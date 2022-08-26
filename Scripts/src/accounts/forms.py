from socket import fromshare
from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User 
        # fields='__all__'
        fields=['first_name','last_name','username','email','password1','password2']
        # exclude=('User permissions','Groups','Password','Last login','Date joined','Staff status','Active')
    
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        # fields='__all__'
        # exclude=('User permissions','Groups','Password','Last login','Date joined','Staff status','Active')
    
    


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image','country','addres']


