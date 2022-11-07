from django import forms 
from django.forms import ModelForm
from .models import Report, BugTracker, EmployeeRequests

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['issuetype','description',]


class EmployeeRequestsForm(forms.ModelForm):
    class Meta:
        model = EmployeeRequests
        fields = ['report']



class BugTrackerForm(forms.ModelForm):
    class Meta:
        model = BugTracker
        fields = ['description']

