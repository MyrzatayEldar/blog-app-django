from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text',
            'id': 'loginName',
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'id': 'loginPassword',
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'surname', 'email',  'username', 'password1', 'password2', 'image', )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'id': 'form3Example1c',
                'class': 'form-control',
                'placeholder': 'Ваше имя'}),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'id': 'last_name',
                'class': 'form-control',
                'placeholder': 'Ваша фамилия'}),
            'surname': forms.TextInput(attrs={
                'type': 'text',
                'id': 'surname',
                'class': 'form-control',
                'placeholder': 'Ваше отчество'}),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'id': 'form3Example3c',
                'class': 'form-control',
                'placeholder': 'Ваша почта'}),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'id': 'username',
                'class': 'form-control',
                'placeholder': 'Имя пользователя'}),
            'password1': forms.TextInput(attrs={
                'id': 'form3Example4c',
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Ваш пароль'}),
            'password2': forms.TextInput(attrs={
                'id': 'form3Example4cd',
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Повторите пароль'}),
            'image': forms.FileInput(attrs={
                'type': 'file',
                'id': 'file',
                'class': 'form-control',
                'placeholder': 'Фото профиля'}),
        }


class PostWritingForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'published_date')
#suckabiglemon