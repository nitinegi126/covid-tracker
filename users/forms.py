from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=70, help_text='Required')
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']