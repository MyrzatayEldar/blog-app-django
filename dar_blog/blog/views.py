from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('username'), password=cd.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
        else:
            return HttpResponse('<h1>User like this doesnt exist.</h1>')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


@login_required(login_url='/')
def main(request):
    return render(request, 'blog/main.html', {})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration success!!')
            return redirect('main')
    else:
        form = RegistrationForm()
    return render(request, 'blog/registration.html', {'form': form})

