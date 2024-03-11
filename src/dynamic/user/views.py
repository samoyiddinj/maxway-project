from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def my_login(request):
    return render(request, 'login.html', {})
