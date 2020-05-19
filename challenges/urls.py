from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "challenges"


urlpatterns = [
    path('', views.ChallengeListView.as_view(), name='challenge-home'),
    path('details/<int:pk>', views.ChallengeDetailsView.as_view(), name='challenge-details'),
    path('pitch/view_pitch/<int:pk>', views.PitchDetailsView.as_view(), name='pitch-details'),
    path('pitch/update_pitch/<int:pk>', views.PitchUpdateView.as_view(), name='pitch-update'),
    path('pitch/delete_pitch/<int:pk>', views.PitchDeleteView.as_view(), name='pitch-delete'),
    path('pitch/final_pitch/<int:pk>', views.FinalPitchUpdateView.as_view(), name='team-pitch'),
    path('pitch/final_pitch_details/<int:pk>', views.FinalPitchDetailsView.as_view(), name='team-pitch-details'),
    path('create_a_challenge', views.ChallengeCreateView.as_view(), name='challenge-create'),
    path('become_a_mentor', views.MentorCreateView.as_view(), name='mentor-create'),
]