from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileRegisterForm, TeamCreateForm, ChangeProfilePicForm
from challenges.forms import Challenge_Verify_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Challenge_Initial_Pitch, Team, Profile
from challenges.models import Challenge
from django.db.models import Q
from django.views.generic import CreateView
from django.utils import timezone
from datetime import datetime, timedelta






# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            profile = Profile.objects.create(user=user, challenge_owner_account=form.cleaned_data['challenge_owner_account'])
            profile.save()
            messages.success(request, f'Your account has been created! You are now logged in!')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            return redirect('challenges:challenge-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, 'title': "Register Now!"})


@login_required
def profile(request):
    if request.user.is_superuser:
        form = TeamCreateForm()
        challenge_form = Challenge_Verify_Form()
        if request.method == 'POST':
            if 'verify_challenge' in request.POST:
                challenge_form = Challenge_Verify_Form(request.POST)
            
            
                if challenge_form.is_valid():
                    chall_to_ver = challenge_form.cleaned_data.get('name')
                    ver_descr_sm = challenge_form.cleaned_data.get('description_small_final')
                    ver_descr_lg = challenge_form.cleaned_data.get('description_large_final')
                    add = challenge_form.cleaned_data.get('admitted')
                    upd_ch = Challenge.objects.filter(name=chall_to_ver).first()
                    upd_ch.description_small_final = ver_descr_sm
                    upd_ch.description_large_final = ver_descr_lg
                    upd_ch.admitted = add
                    upd_ch.save()
            
            elif 'add_team_member' in request.POST:
                form = TeamCreateForm(request.POST)


                if form.is_valid():
                    ch = form.cleaned_data.get('team')
                    member = form.cleaned_data.get('new_member')
                    challenge = form.cleaned_data.get('challenge')
                    if ch=='new team':
                        new_team = Team.objects.create(challenge=Challenge.objects.filter(name=challenge).first())
                        new_team.members.add(User.objects.filter(username=member).first().profile)
                        new_team.save()
                        form = TeamCreateForm()
                    else:
                        new_team = Team.objects.filter(pk=ch).first()
                        if new_team.members.count() < 3:
                            new_team.members.add(User.objects.filter(username=member).first().profile)
                            new_team.save()
                            form = TeamCreateForm()
                        else:
                            messages.warning(request, f'Team has 3 members already')

        return render(request, 'users/profile_admin.html', {'pitch_list': Challenge_Initial_Pitch.objects.all(), 'teams_list': Team.objects.all(), 'challenge_list': Challenge.objects.all(), 'form': form, 'challenge_form':challenge_form, 'tz': timezone.now(), 'title': "Profile"  })

    
    
    if request.user.profile.challenge_owner_account:
        return render(request, 'users/profile_challenge_owner.html', {'pitch_list': Challenge_Initial_Pitch.objects.filter(user=request.user), 'teams_list': Team.objects.filter(members=request.user.profile), 'owned_challenge_teams_list': Team.objects.filter(challenge__in=request.user.owned_challenges.all()), 'title': "Profile", 'active_challenge': Challenge.objects.filter((Q(applicants = request.user) & Q(due_date__gte=datetime.now()))), 'past_challenges': Challenge.objects.filter((Q(applicants = request.user) & Q(due_date__lte=datetime.now()))) })


    act_challenge = Challenge.objects.filter((Q(applicants = request.user) & Q(due_date__gte=datetime.now()))).first()


    return render(request, 'users/profile.html', {'pitch_list': Challenge_Initial_Pitch.objects.filter(user=request.user), 'teams_list': Team.objects.filter(members=request.user.profile), 'title': "Profile", 'active_challenge': Challenge.objects.filter((Q(applicants = request.user) & Q(due_date__gte=datetime.now()))), 'past_challenges': Challenge.objects.filter((Q(applicants = request.user) & Q(due_date__lte=datetime.now()))), 'active_team': Team.objects.filter(Q(challenge = act_challenge) & Q(members=request.user.profile)) })




