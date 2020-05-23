from django import forms
from django.forms import ModelForm
from .models import Challenge


class Challenge__Form(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'assignor', 'description_small', 'description_large', 'assignor_website', 'due_date', 'category']
    


class Challenge_Verify_Form(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'description_small_final', 'description_large_final', 'admitted']
        widgets = {
            'name': forms.HiddenInput,
        }