from django.db.models import Q
from accounts.models import Profile
from .models import *


def searchAll(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    employees = Profile.objects.filter(Q(name__iexact=search_query))
    reports = Report.objects.filter(issuetype__iexact=search_query)
    bugs = BugTracker.objects.filter(description__iexact=search_query)
    requests = EmployeeRequests.objects.filter(report__iexact=search_query)
    tasks = Task.objects.filter(
    Q(name__iexact=search_query)
    |Q(description__iexact=search_query)
    |Q(in_charge__username__iexact=search_query))
    departments = Department.objects.filter(name__iexact=search_query)
    return employees,reports,bugs,requests,tasks,departments,search_query