from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'surname', 'email',  'username', 'password1', 'password2', 'image', )
