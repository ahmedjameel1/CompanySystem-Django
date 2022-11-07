from django.shortcuts import render, redirect
from .models import Department , Task, Report, EmployeeRequests, BugTracker
from accounts.models import Profile
from django.contrib import messages
from .forms import ReportForm, BugTrackerForm, EmployeeRequestsForm

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html',{'departments':Department.objects.all()})


def department(request,depart_id):
    department = Department.objects.get(id=depart_id)
    tasks = department.tasks.all()
    colleagues = department.colleagues.all()
    ctx = {'department': department,  'colleagues':colleagues,'tasks':tasks}
    return render(request, 'dashboard/department.html', ctx)


def task(request, task_id):
    task = Task.objects.get(id=task_id)
    users = Profile.objects.all()
    print(users)
    return render(request, 'dashboard/singletask.html',{'task': task,'users':users})

def changeStatus(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        if request.POST.get('status'):
            status = request.POST.get('status')
            task.status = status
        if request.POST.get('in_charge'):
            in_charge = request.POST.get('in_charge')
            task.in_charge = Profile.objects.get(username=in_charge)
        task.save()
        return redirect('singletask', task.id)

    
def employee(request,pk):
    employee = Profile.objects.get(id=pk)
    task = Task.objects.get(in_charge=employee)
    department = employee.depart
    return render(request,'dashboard/employeeinfo.html',{
        'employee': employee,'task':task,'department':department})


def progressReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.issued_by = request.user.profile
            report.save()
            messages.success(request,'report submitted!')
            return redirect('dashboard')
    else:
        form = ReportForm()
    return render(request,'dashboard/form.html',{'form':form})

def employeeRequest(request):
    if request.method == 'POST':
        form = EmployeeRequestForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.requested_by = request.user.profile
            report.save()
            messages.success(request,'request submitted!')
            return redirect('dashboard')
    else:
        form = EmployeeRequestFrom()
    return render(request,'dashboard/form.html',{'form':form})


def bugReport(request):
    if request.method == 'POST':
        form = BugTreckerForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.issued_by = request.user.profile
            report.department = request.user.department
            report.save()
            messages.success(request,'report submitted!')
            return redirect('dashboard')
    else:
        form = BugTrackerForm()
    return render(request,'dashboard/form.html',{'form':form})



def bugs(request):
    bugs = BugTracker.objects.all()
    return render(request, 'dashboard/bugslist.html',{'bugs':bugs})

def requests(request):
    requests = EmployeeRequests.objects.all()
    return render(request, 'dashboard/requestslist.html',{'requests':requests})


def reports(request):
    reports = Report.objects.all()
    return render(request, 'dashboard/reportslist.html',{'reports':reports})

def bugStatus(request, bug_id):
    bug = BugTracker.objects.get(id=bug_id)
    if request.method == 'POST':
        if request.POST.get('status'):
            status = request.POST.get('status')
            bug.status = status
            bug.save()
        return redirect('bugs')

def reportStatus(request, report_id):
    report = Report.objects.get(id=report_id)
    if request.method == 'POST':
        if request.POST.get('status'):
            status = request.POST.get('status')
            report.status = status
            report.save()
        return redirect('reports')


def requestStatus(request, request_id):
    request = EmployeeRequests.objects.get(id=request_id)
    if request.method == 'POST':
        if request.POST.get('status'):
            status = request.POST.get('status')
            request.status = status
            request.save()
        return redirect('requests')