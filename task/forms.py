from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('id','title','task_status','created_at')

