from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.hashers import make_password


# Create your views here.


def indexview(request):
    return render(request, 'index.html')


def registerview(request):
    if request.POST:
        model = User()
        model.username = request.POST['name']
        model.email = request.POST['email1']
        model.password = make_password(request.POST['pass'])
        model.save()
        return redirect('login')
    return render(request, 'register.html')


def loginview(request):
    if request.method == 'POST':
        loginusername = request.POST['your_name']
        print("Username",loginusername)
        loginpassword = request.POST['your_pass']
        print("Password",loginpassword)

        user = authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

# def loginview(request):
#     if request.method == 'POST':
#         userrr = request.POST['your_name']
#         pas = request.POST['your_pass']
#         user = auth.authenticate(username=userrr, password=pas)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.info(request, "Invalid credentials")
#             return redirect('login')
#     return render(request, 'login.html')


def dashboardview(request):
    return render(request, 'dashboard.html')


def logoutview(request):
    logout(request)
    return redirect('login')
