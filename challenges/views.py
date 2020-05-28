from django.shortcuts import render, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormMixin
from .models import Challenge, Mentor
from users.models import Challenge_Initial_Pitch, Team, Notifications
from users.forms import Challenge_Initial_Pitch_Form, FinalPitchForm
from django.db.models import Q
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
# Create your views here.



class ChallengeListView(ListView):
    queryset = Challenge.objects.filter(admitted=True)
    template_name = 'challenges/challenge_list.html'
    ordering = ['-date_posted']
    paginate_by = 6


    # def get_context_data(self, **kwargs):
    #     context = super(ChallengeListView, self).get_context_data(**kwargs)
    #     context['curr_date'] = timezone.now()
    #     return context



class ChallengeDetailsView(FormMixin, DetailView):
    model = Challenge
    template_name = 'challenges/challenge_details.html'
    form_class = Challenge_Initial_Pitch_Form

    def get_success_url(self):
        return reverse('challenges:challenge-details', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ChallengeDetailsView, self).get_context_data(**kwargs)
        context['form'] = Challenge_Initial_Pitch_Form()
        self.object = self.get_object()
        context['title'] = self.object.name
        if self.request.user.is_authenticated:
            now = timezone.now()
            if (self.object.due_date.date() > now.date()):
                context['curr_active']=True
            else:
                context['curr_active']=False
        



            if (self.object.apply_until_date.date() > now.date()):
                context['applications_open']=True
            else:
                context['applications_open']=False
        


            if self.request.user.challenges.all():
                for ch in self.request.user.challenges.all():
                    if (ch.due_date.date() > now.date()):
                        context['active']= True
                    else:
                        context['active'] = False
            else:
                context['active'] = False
                    
            context['pitch_list'] = Challenge_Initial_Pitch.objects.filter(Q(challenge=self.object) & Q(user=self.request.user))
            context['teams_list'] = Team.objects.filter(Q(members=self.request.user.profile) & Q(challenge=self.object))
            context['owned_challenge_teams_list'] = Team.objects.filter(Q(challenge=self.object))
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, f'Your Application has been submitted!')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.challenge = self.object
        self.object.applicants.add(self.request.user)
        form.save()
        return super().form_valid(form)




class PitchDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Challenge_Initial_Pitch
    template_name = 'users/initial_pitch_details.html'

    def get_context_data(self, **kwargs):
        context = super(PitchDetailsView, self).get_context_data(**kwargs)
        context['title'] = 'View your application'
        return context


    def test_func(self):
        pitch = self.get_object()
        # diag = self.request.user.challenges.filter(name=pitch.challenge.name).first()
        # team = self.request.user.profile.teams.filter(challenge=diag).first()
        if ((self.request.user == pitch.user)):
            return True
        return False




class PitchUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Challenge_Initial_Pitch
    fields = ['written_pitch']
    success_message = "Your application was updated successfully!"

    def get_context_data(self, **kwargs):
         context = super(PitchUpdateView, self).get_context_data(**kwargs)
         context['title'] = 'Update your application'
         return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def test_func(self):
        pitch = self.get_object()
        diag = self.request.user.challenges.filter(name=pitch.challenge.name).first()
        team = self.request.user.profile.teams.filter(challenge=diag).first()
        if ((self.request.user == pitch.user) and (not team)):
            return True
        return False
    
        
    def get_success_url(self):
        return reverse('profile')




class PitchDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Challenge_Initial_Pitch
    success_message = "Application deleted"

    def get_context_data(self, **kwargs):
        context = super(PitchDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete your application'
        return context

    def test_func(self):
        pitch = self.get_object()
        if self.request.user == pitch.user:
            return True
        return False
    
    def get_success_url(self):
        return reverse('challenges:challenge-details', kwargs={'pk': self.object.challenge.pk})
    
    def delete(self, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        self.object = self.get_object()
        self.object.challenge.applicants.remove(self.request.user)
        if self.object.user.profile.teams.filter(challenge = self.object.challenge).first():
            temp_id = self.object.user.profile.teams.filter(challenge = self.object.challenge).first().id
            self.object.user.profile.teams.filter(challenge = self.object.challenge).first().members.remove(self.request.user.profile)
            if self.object.challenge.challenge_teams.filter(id = temp_id).first().members.count() == 0:
                self.object.challenge.challenge_teams.filter(id = temp_id).first().delete()
        return super(PitchDeleteView, self).delete(*args, **kwargs)



class ChallengeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Challenge
    fields = ['name', 'description_small', 'description_large', 'assignor_website', 'due_date', 'category', 'contact_person_full_name', 'contact_person_email']
    success_message = "%(name)s was submitted successfully!"

    def get_context_data(self, **kwargs):
        context = super(ChallengeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Submit a new challenge'
        return context


    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.assignor = self.request.user 
        return super(ChallengeCreateView, self).form_valid(form)


    def get_success_url(self):
        return reverse('challenges:challenge-home')




class FinalPitchDetailsView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = 'challenges/final_team_pitch_details.html'



class FinalPitchUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Team
    form_class = FinalPitchForm
    template_name = 'challenges/final_pitch.html'

    def test_func(self):
        team = self.get_object()
        if self.request.user.profile in team.members.all():
            return True
        return False

    def get_success_url(self):
        return reverse('profile')
    
    def get_form_kwargs(self):
        kwargs = super(FinalPitchUpdateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(FinalPitchUpdateView, self).get_context_data(*args, **kwargs)
        team = self.get_object()
        context['team_signs'] = team.signs.count
        context['title'] = 'Submit your Solution'
        return context




class MentorCreateView(SuccessMessageMixin, CreateView):
    model = Mentor
    fields = ['first_name', 'last_name', 'bio', 'contact_email', 'profile_image']
    success_message = "Your application to participate as a mentor was was submitted successfully!"

    def get_context_data(self, *args, **kwargs):
        context = super(MentorCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Help our teams grow!'
        return context

    def get_success_url(self):
        return reverse('challenges:challenge-home')



