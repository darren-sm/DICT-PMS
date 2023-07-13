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
        foo.id = cpms_data['id']
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
def form(request, category, method = 'add', key = None):
    if request.user.is_authenticated:
        
        categories = {
            'cpms': {
                'model': CPMS,
                'form': CPMSForm,
                'html': 'cpms_form.html',
                'key': 'id'
            },
            'examinee': {
                'model': Examinees,
                'form': ExamineesForm,
                'html': 'examinees_form.html',
                'key': 'no'
            },
            'ojt': {
                'model': OJTInput,
                'form': OJTInputForm,
                'html': 'ojt_input_form.html',
                'key': 'id'
            }
        }
        item = {'method': method, 'model': category}
        target_record = None
        if method == 'update':       
            target_record = categories[category]['model'].objects.get(**{categories[category]['key']: key})
            item['key'] = key            
        
        if category == 'cpms':
            item['flattened_cpms'] = _flatten_cpms(target_record.__dict__)
            
        if request.method == "POST":
            if category == 'cpms':                
                form = CPMSForm({
                    'program': request.POST['Program'],
                    'info': {
                        'Activity': request.POST.getlist('Activity[]'),
                        'Indicator': request.POST.getlist('Indicator[]'),
                        'Target': request.POST.getlist('Target[]'),
                        'Accomplishment': request.POST.getlist('Accomplishment[]'),
                        'Remarks': request.POST.getlist('Remarks[]')
                    }
                }, instance = target_record)       
            else:
                form = categories[category]['form'](request.POST, instance = target_record)
            
            if form.is_valid():
                form.save()
                return redirect('home')     
            else:
                print(form.errors)    
        else:            
            form = categories[category]['form'](request.POST or None, instance=target_record)
        item['form'] = form
        return render(request, categories[category]['html'], item)

    messages.error("You need to login to access that")
    return redirect('home') 

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


def record(request, category, primary_key):
    if request.user.is_authenticated:
        categories = {
            'cpms': {
                'class': CPMS, 
                'selector': 'id', 
                'name': 'CPMS',
                'keys': ['program', 'info.Target']
                },
            'examinee': {
                'class': Examinees, 
                'selector': 'no', 
                'name': 'Examinee',
                'keys': ['province', 'component', 'name', 'venue', 'gender', 'date', 'time', 'status', 'remarks', 'batch']
                },
            'ojt': {
                'class': OJTInput, 
                'selector': 'id',
                'name': 'OJT Input',
                'keys': ['province', 'category', 'suc', 'duration', 'school_address', 'representative', 'representative_contact', 'student_name', 'sex', 'student_contact', 'start_date', 'end_date', 'mode', 'resume', 'endorsement', 'moa', 'remarks']
                }
        }
        target_record = categories[category]['class'].objects.get(**{categories[category]['selector']: primary_key})
        if category == "cpms":
            flattened_cpms = _flatten_cpms(target_record.__dict__)
        return render(request, 'record.html', 
                      {'record': target_record, 
                       'name': categories[category]['name'],
                       'flattened_cpms': flattened_cpms if category == "cpms" else None,
                       'category':category,
                       'key': target_record.id if category in ('cpms', 'ojt') else target_record.no,
                       'keys': categories[category]['keys']
                       })
    return redirect('login')


def delete_record(request, category, primary_key):
    if request.user.is_authenticated:
        categories = {
            'cpms': {
                'class': CPMS, 
                'selector': 'id'
                },
            'examinee': {
                'class': Examinees, 
                'selector': 'no', 
                },
            'ojt': {
                'class': OJTInput, 
                'selector': 'id',
                }
        }
        target_record = categories[category]['class'].objects.get(**{categories[category]['selector']: primary_key})
        target_record.delete()
        messages.success(request, "Record deleted succesfully")
        return redirect('home')
    
    return redirect('login')
