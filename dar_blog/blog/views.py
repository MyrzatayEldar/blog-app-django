from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
    posts = Post.objects.all()
    user = request.user
    categories = Category.objects.all()
    context = {
        'title': f'{user}\'s page',
        'posts': posts,
        'cats': categories,
        'number': 25
    }
    return render(request, 'blog/main.html', context)


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


def show_test_page(request):
    return render(request, 'blog/test.html', {})


@login_required(login_url='/')
def write_post(request):
    if request.method == 'POST':
        form = PostWritingForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = PostWritingForm
    return render(request, 'blog/write_post.html', {'form': form,
                                                    'title': 'Страница написания поста'})


@login_required(login_url='/')
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AddCategoryForm
    return render(request, 'blog/add_cat.html', context={'form': form,
                                                         'title': 'Добавить категорию'})


@login_required(login_url='/')
def detail_category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    context = {
        'obj': obj,
        'title': f'Категория - {obj.name}'
    }
    if request.method == 'POST':
        obj.delete()
        return redirect('main')
    return render(request, 'blog/delete_cat.html', context)


@login_required(login_url='/')
def show_post(request, pk):
    obj = get_object_or_404(Post, pk=pk)
    context = {
        'obj': obj
    }
    return render(request, 'blog/show_post.html', context)