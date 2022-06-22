from django.shortcuts import render


def login(request):
    return render(request, 'blog/login.html', {})


def main(request):
    return render(request, 'blog/main.html', {'a': 25})