from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Rating

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]

class CreateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=["name", "projects"]
        fields=["bio", "profile_pic", "contact"]

class UploadNewProject(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['design_rating', 'usability_rating', 'content_rating', 'average_review', 'profile']
        fields=['title', 'image', 'description', 'link'] 
