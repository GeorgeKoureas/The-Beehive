from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.apps import apps
# Create your models here.





class Challenge(models.Model):
    name = models.CharField(max_length=30)
    assignor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='owned_challenges')
    description_small = models.TextField()
    description_small_final = models.TextField(blank=True)
    description_large = models.TextField()
    description_large_final = models.TextField(blank=True)
    assignor_website = models.URLField()
    due_date = models.DateTimeField()
    apply_until_date = models.DateTimeField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    applicants = models.ManyToManyField(User, blank=True, related_name='challenges')
    admitted = models.BooleanField(default=False, blank=True)
    contact_person_full_name = models.CharField(max_length=50, null=True)
    contact_person_email = models.EmailField(null=True)
    cover_image = models.ImageField(default='default_challenge.jpg', upload_to='challenge_pics')
    prize = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    





class Mentor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    contact_email = models.EmailField()
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    admitted = models.BooleanField(default=False, blank=True)
    
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} - Mentor'

