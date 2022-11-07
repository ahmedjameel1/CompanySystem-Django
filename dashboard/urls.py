from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('department/<int:depart_id>/', views.department, name='department'),
    path('task/<int:task_id>/', views.task, name='singletask'),
    path('changestatus/<int:task_id>/', views.changeStatus, name='taskstatus'),
    path('reportchange/<int:report_id>/', views.reportStatus, name='reportstatus'),
    path('bugchange/<int:bug_id>/', views.bugStatus, name='bugstatus'),
    path('requestchange/<int:request_id>/', views.requestStatus, name='requeststatus'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('reportprogress/', views.progressReport, name='progressreport'),
    path('requestsubmit/', views.employeeRequest, name='requestsubmit'),
    path('bugreport/', views.bugReport, name='bugreport'),
    path('bugs/', views.bugs, name='bugs'),
    path('requests/', views.requests, name='requests'),
    path('reports/', views.reports, name='reports'),





]
