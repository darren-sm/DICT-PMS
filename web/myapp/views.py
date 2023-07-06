from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#homeview
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {})
    else:
        return redirect('login')

#loginbackend
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {})
    messages.error(request, "You have to log in first to access that")
    return redirect('login')

def report(request):
    if request.user.is_authenticated:
        return render(request, 'report.html', {})
    messages.error(request, "You have to log in first to access that")
    return redirect('login')