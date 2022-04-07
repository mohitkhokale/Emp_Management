from django.shortcuts import render ,redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
from task.models import Task 
class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'home-page.html'

    def get(self,request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request,self.template_name,context)


    def post(self,request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('dashboard')                
        context = {
            'form':form,  
        }
        return render(request,self.template_name,context)

def LogoutView(request):
    logout(request)
    return redirect('homepage')

def DashboardView(request):
    open_task =Task.objects.filter(admin_id=request.user.id,task_status='OPEN').count()
    inprogress_task =Task.objects.filter(admin_id=request.user.id,task_status='IN-PROGRESS').count()
    completed_task =Task.objects.filter(admin_id=request.user.id,task_status='COMPLETED').count()
    staff_count = User.objects.filter(is_staff=False).count()
   
    assigned_user = User.objects.all().values('id','username').order_by('id')
  
    task_details = Task.objects.distinct().select_related('admin_id').values('admin_id')
  


    context = { 
        'count':staff_count,
        'open_task':open_task,
        'inprogress_task':inprogress_task,
        'completed_task':completed_task,
        'assigned_user':assigned_user,
        'task_details':task_details
    }

    return render(request,'dashboard.html',context)
