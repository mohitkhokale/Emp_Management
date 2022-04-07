from .models import Task
from django.shortcuts import redirect, render
from django.views import View
from .forms import TaskForm
from django.contrib.auth.models import User
# Create your views here.

class TaskView(View):
    form_class = TaskForm
    template_name = 'task.html'
    def get(self, request,id=None):
        form_class = self.form_class()
        form = Task.objects.filter(admin_id=request.user.id)

        if form_class.is_valid():
            form_class.save()
        context = {
            'form_class': form_class,
            'form': form,
         }

        return render(request,self.template_name,context)

def update_task(request,task_id=None):

    profile_id = Task.objects.get(pk=task_id)
    form_class = TaskForm(data = request.POST or None,instance=profile_id)
    if form_class.is_valid():
        form_class.save()
        return redirect('task') 
    context = {
            'form_class':form_class
        }
    return render(request,'update_task.html',context)
    


    # if request.method == 'GET':
        # Product_Category = Task.objects.all()
        # form_data = Task(request.POST or None)
        # print("yes1",form_data)
        # if form_data.is_valid():
        #     print("yes")
        #     form_data.save()
        #     context = {
        #         'form_data':form_data
        #     }
        #     return render(request,'update_task.html',context)
        # else:
        #     return render(request,'update_task.html')

    # else:
    #     return render(request,'task.html')

# def DashboardView(request):
#     open_task =Task.objects.filter(employee=request.user.id,task_status='OPEN').count()
#     inprogress_task =Task.objects.filter(employee=request.user.id,task_status='IN-PROGRESS').count()
#     completed_task =Task.objects.filter(employee=request.user.id,task_status='COMPLETED').count()
#     staff_count = User.objects.filter(is_staff=False).count()
#     userList = User.emp.all()
 
#     print("userList-->>>",userList)
    
#     context = { 
#         'count':staff_count,
#         'open_task':open_task,
#         'inprogress_task':inprogress_task,
#         'completed_task':completed_task,
#         'userList':userList
#     }
#     return render(request,'dashboard.html',context)