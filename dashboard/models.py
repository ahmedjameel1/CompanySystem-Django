from django.db import models
from accounts.models import Profile
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey("accounts.Profile",on_delete=models.CASCADE, null=True, blank=True)
    tasks = models.ManyToManyField('Task', blank=True)
    colleagues = models.ManyToManyField("accounts.Profile",blank=True, related_name='colleagues')

    def __str__(self):
        return self.name

STATUS = (
    ('in progress','in progress'),
    ('done','done'),
    ('delayed','delayed'),
    ('queued','queued'),
    ('under review','under review'),
    ('accepted','accepted'),
    ('refused','refused'),
    ('open','open'),
    ('closed','closed'),
    ('solved','solved')
)

class Task(models.Model):
    in_charge = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=True,null=True)
    status = models.CharField(max_length=50,choices=STATUS,default='queued')
    deadline = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmployeeRequests(models.Model):
    requested_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=50,choices=STATUS,default='open')
    report = models.TextField(max_length=300,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.requested_by)
    

class BugTracker(models.Model):
    issued_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    status= models.CharField(max_length=50,choices=STATUS,default='open')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.description




class Report(models.Model):
    status = models.CharField(max_length=50,choices=STATUS,default='open')
    issued_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    issuetype = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(max_length=255,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.issuetype
