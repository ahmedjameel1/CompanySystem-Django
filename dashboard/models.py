from django.db import models
from accounts.models import Profile
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    tasks = models.ManyToManyField('Task', blank=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE, null=True, blank=True)
    colleagues = models.ManyToManyField(Profile,blank=True, related_name='colleagues')
    leader = models.ForeignKey(Profile , on_delete=models.CASCADE,null=True, blank=True)


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
    ('closed','closed')
)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=True,null=True)
    status = models.CharField(max_length=50,choices=STATUS,default='queued')
    deadline = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmployeeRequests(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50,choices=STATUS,default='under review')
    report = models.TextField(max_length=300,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


