from django.contrib import admin
from .models import Profile, Team
from .models import Challenge_Initial_Pitch, Notifications
# Register your models here.
admin.site.register(Profile)
admin.site.register(Notifications)
admin.site.register(Team)
admin.site.register(Challenge_Initial_Pitch)
