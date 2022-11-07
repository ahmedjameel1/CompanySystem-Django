from django.contrib import admin
from .models import * 

# Register your models here.

class BugTrackerAdmin(admin.ModelAdmin):
    list_display = ['department', 'issued_by', 'description', 'updated', 'status']
    list_editable = ['status',]

admin.site.register(Department)
admin.site.register(Task)
admin.site.register(BugTracker,BugTrackerAdmin)
admin.site.register(EmployeeRequests)
admin.site.register(Report)