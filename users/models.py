from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from challenges.models import Challenge
# Create your models here.


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    challenge_owner_account = models.BooleanField(null=True, help_text='Selecting YES will allow you to submit challenges!, Selecting NO will allow you to solve a challenge')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Team(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True, related_name='challenge_teams')
    members = models.ManyToManyField(Profile, blank=True, related_name='teams')
    final_written_pitch = models.TextField(blank=True)
    signs = models.ManyToManyField(Profile, blank=True)


    def __str__(self):
        count = 1
        # if self.challenge.challenge_teams:
        for team in self.challenge.challenge_teams.all():
            if team.id != self.id:
                count += 1
            else: 
                break
        return f'Team {count}'


class Challenge_Initial_Pitch(models.Model):
    written_pitch = models.TextField()
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='individual_pitch')

    def __str__(self):
        return f'"{self.user.username}" pitch for "{self.challenge.name}" challenge'



class Notifications(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)