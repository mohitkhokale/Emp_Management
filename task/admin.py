from django.contrib import admin
from task.models import Task 

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_status','admin','created_at','date_of_submit')
admin.site.register(Task,TaskAdmin)

# class assigntaskAdmin(admin.ModelAdmin):
#     list_display = ('task', 'admin')
# admin.site.register(assignTask,assigntaskAdmin)