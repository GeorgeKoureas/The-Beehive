from django import forms
from django.forms import ModelForm
from django.forms.widgets import Select, CheckboxSelectMultiple, CheckboxInput, mark_safe
from .models import Profile, Challenge_Initial_Pitch, Team
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from itertools import chain
from django.utils.encoding import force_str
from django.utils.html import escape, conditional_escape
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field




CHOICES = (
            (False, 'Solve a challenge'),
            (True, 'Create a challenge'),
        )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    challenge_owner_account = forms.ChoiceField(choices=CHOICES, label='I want to:')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data



class ChangeProfilePicForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ProfileRegisterForm(ModelForm):
    #image = forms.ImageField(required=False)
    challenge_owner_account = forms.ChoiceField(choices=CHOICES, help_text='Selecting YES will allow you to submit challenges!, Selecting NO will allow you to solve a challenge')

    class Meta:
        model = Profile
        fields = [ 'challenge_owner_account']



class Challenge_Initial_Pitch_Form(ModelForm):
    class Meta:
        model = Challenge_Initial_Pitch
        fields = ['written_pitch']
        widgets = {
            'written_pitch': forms.Textarea(attrs={'rows': 3}),
        }






class CheckboxCustom(forms.SelectMultiple):
    

    def __init__(self, *args, **kwargs):
        self.input_type = 'checkbox'
        self.checked_attribute = {'checked': True}
        self.template_name = 'django/forms/widgets/checkbox_select.html'
        self.option_template_name = 'django/forms/widgets/checkbox_option.html'
        self.allow_multiple_selected = True
        self.request = kwargs.pop("request")
        self.option_inherits_attrs = False
        # print(options
        super(CheckboxCustom, self).__init__(*args, **kwargs)
    

    def create_option(self, *args, **kwargs):
        options_dict = super().create_option(*args, **kwargs)
        selected = options_dict['selected']
        value = options_dict['value']
        # option_attrs = self.build_attrs(self.attrs, attrs) if self.option_inherits_attrs else {}

        if options_dict['label'] != str(self.request.user.profile):
            # options_dict['attrs']['onclick'] = 'return false;'
            options_dict['attrs']['class'] = 'readonly'
        
        return options_dict
    
    

    
        


class TeamCreateForm(forms.Form):
    team = forms.ChoiceField()
    new_member = forms.CharField(widget=forms.HiddenInput())
    challenge = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(TeamCreateForm, self).__init__(*args, **kwargs)
        self.fields['team'].choices = [('new team', 'Create New')] + [(choice.pk, choice) for choice in Team.objects.all()]

    






class FinalPitchForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['final_written_pitch', 'signs']


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FinalPitchForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            team = kwargs['instance']
            self.fields['signs'].widget = CheckboxCustom(request=self.request)
            self.fields['signs'].queryset = team.members.all()
            queryset = team.members.all()
            # self.fields['signs'] = ModelMultipleChoiceField(queryset)

            for item in queryset:
                if(self.fields['signs'].choices.choice(item)[1]) == str(self.request.user.profile):
                    # self.fields['signs'].choices.attrs['disabled'] = True
                    print(self.fields['signs'].choices.choice(item))


    


