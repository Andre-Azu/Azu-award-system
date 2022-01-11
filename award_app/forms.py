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
        #exclude=["name", "projects"]
        fields=["bio", "profile_pic", "contact"]