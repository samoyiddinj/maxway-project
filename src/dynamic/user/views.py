from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        form.save()
        return redirect('login')

    ctx = {
        'form': form
    }
    return render(request, 'register.html', ctx)


def my_login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('index')
    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)
