from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CPMSForm, ExamineesForm, OJTInputForm
from .models import CPMS, Examinees, OJTInput

# Home View (index.html)
def _flatten_cpms(cpms_data):
    bar = []
    for i in range(len(cpms_data['info']['Activity'])):
        class foo:
            pass
        if i == 0:
            foo.Program = cpms_data['program']
        else:
            foo.Program = ''
        foo.Activty = cpms_data['info']['Activity'][i]
        foo.Indicator = cpms_data['info']['Indicator'][i]
        foo.Target = cpms_data['info']['Target'][i]
        foo.Accomplishment = cpms_data['info']['Accomplishment'][i]
        foo.Remark = cpms_data['info']['Remarks'][i]
        bar.append(foo)
    return bar

def home(request):
    if request.user.is_authenticated:
        cpms_data = [_flatten_cpms(obj.__dict__) for obj in CPMS.objects.all()]
        examinees_data = Examinees.objects.all()
        ojt_data = OJTInput.objects.all()
        return render(request, 'index.html', {
            'cpms_data': cpms_data,
            'examinees_data': examinees_data,
            'ojt_data': ojt_data
        })
    else:
        return redirect('login')


# Log in (login.html); Redirect to home if user is authenticated
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

# Input Page (contains the forms)
def inputdata(request):
    if request.user.is_authenticated:
        return render(request, 'inputdata.html', {})
    messages.error(request, "You have to log in first to access that")
    return redirect('login')


# (Input Form) CPMS Data
def cpms_create_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_data = {
                'program': request.POST['Program'],
                'info': {
                    'Activity': request.POST.getlist('Activity[]'),
                    'Indicator': request.POST.getlist('Indicator[]'),
                    'Target': request.POST.getlist('Target[]'),
                    'Accomplishment': request.POST.getlist('Accomplishment[]'),
                    'Remarks': request.POST.getlist('Remarks[]')
                }
            }
            print(form_data)
            form = CPMSForm(form_data)
            if form.is_valid():
                form.save()
                return redirect('home')             
        else:
            form = CPMSForm()
        return render(request, 'cpms_form.html', {'form': form})
    else:
        return redirect('login')

# (Input Form) Examinee Data
def examinees_create_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_data = {
                'province': request.POST['province'],
                'component': request.POST['component'],
                'name': request.POST['examinee_name'],
                'venue': request.POST['venue'],
                'gender': request.POST['gender'],
                'date': request.POST['datepicker'],
                'time': request.POST['time'],
                'status': request.POST['status'],
                'remarks': request.POST['remarks'],
                'batch': request.POST['batch'],
            }
            form = ExamineesForm(form_data)
            if form.is_valid():
                form.save()
                return redirect('home')  
            else:
                print(form.errors)
        else:
            form = ExamineesForm()
        return render(request, 'examinees_form.html', {'form': form})
    else:
        return redirect('login')


# (Input Form) CPMS Data
def ojt_input_create_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_data = {
                'province': request.POST['province'],
                'category': request.POST['category'],
                'suc': request.POST['suc'],
                'duration': request.POST['duration'],
                'school_address': request.POST['school_address'],
                'representative': request.POST['representative'],
                'representative_contact': request.POST['representative_contact'],
                'student_name': request.POST['student_name'],
                'sex': request.POST['sex'],
                'student_contact': request.POST['student_contact'],
                'start_date': request.POST['start_date'],
                'end_date': request.POST['end_date'],
                'mode': request.POST['mode'],
                'resume': request.POST.get('resume') == 'true',
                'endorsement': request.POST.get('endorsement') == 'true',
                'moa': request.POST.get('resume') == 'true',
                'remarks': request.POST['remarks'],
            }
            print(form_data)
            form = OJTInputForm(form_data)
            if form.is_valid():
                form.save()
                return redirect('home')  
            else:
                print(form.errors)
        else:
            form = OJTInputForm()
        return render(request, 'ojt_input_form.html', {'form': form})
    else:
        return redirect('login')

# Dashboard page (dashboard.html)
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {})
    messages.error(request, "You have to log in first to access that")
    return redirect('login')

# Report page (report.html)
def report(request):
    if request.user.is_authenticated:
        return render(request, 'report.html', {})
    messages.error(request, "You have to log in first to access that")
    return redirect('login')