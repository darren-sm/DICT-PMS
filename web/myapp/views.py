from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {})
    else:
        return redirect('login')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('login')