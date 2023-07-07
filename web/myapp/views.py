from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CPMSForm, ExamineesForm, OJTInputForm
from .models import CPMS, Examinees, OJTInput

#homeview
def home(request):
    if request.user.is_authenticated:
        cpms_data = CPMS.objects.all()
        examinees_data = Examinees.objects.all()
        ojt_data = OJTInput.objects.all()
        return render(request, 'index.html', {
            'cpms_data': cpms_data,
            'examinees_data': examinees_data,
            'ojt_data': ojt_data
        })
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

#Input Forms

def cpms_create_view(request):
    if request.method == 'POST':
        form = CPMSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = CPMSForm()
    return render(request, 'cpms_form.html', {'form': form})

def examinees_create_view(request):
    if request.method == 'POST':
        form = ExamineesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ExamineesForm()
    return render(request, 'examinees_form.html', {'form': form})

def ojt_input_create_view(request):
    if request.method == 'POST':
        form = OJTInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = OJTInputForm()
    return render(request, 'ojt_input_form.html', {'form': form})

#Dashboard Backend

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

def inputdata(request):
    if request.user.is_authenticated:
        return render(request, 'inputdata.html', {})
    messages.error(request, "You have to log in first to access that")
    return redirect('login')
