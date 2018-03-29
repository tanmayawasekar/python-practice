# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView, LogoutView, UserModel

from django import forms

# Create your views here.

def index(request):
    return render(request, 'authenticate/index.html')

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()


def register(request):
    form = UserForm(request.POST)
    print(request.POST)
    print(form.is_valid(), "form.isseee")
    if form.is_valid():
        form.save()
        user_name = form.cleaned_data.get('username')
        password = form.clean_password2()
        print(password)
        print(user_name)
        user = authenticate(username=user_name, password=password)
        print(user)
        login(request, user)
        return redirect('/polls/')
    else:
        return render(request, 'authenticate/register.html', {"form":form})

class loginView(LoginView):
    template_name = 'authenticate/login.html'

class logoutView(LogoutView):
    is_staff = False
