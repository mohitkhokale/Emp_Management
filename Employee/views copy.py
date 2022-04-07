from tkinter.messagebox import NO
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from Employee.forms import EmployeeForm
from Employee.models import Employee
 
# Create your views here.
   
def emp_update(request,pk=None):
#   // working
    try:
            Product_Category = Employee.objects.get(pk=pk) 
            form_class = EmployeeForm(request.POST or None,instance=Product_Category)        
            print(form_class)
            if form_class.is_valid():
                form_class.save()   
            context ={
            'form':form_class,
            }
            return render(request,'Employee.html',context)
          
    except Exception as e:
        return render(request,'Employee.html',)


    #  user = Employee.objects.get(pk=pk)
    #     if request.user.id == user.id:
    #         profile_id = Employee.objects.get(pk=pk)
    #         user_img = Employee.objects.filter(pk=pk)
         
    #         form_class = EmployeeForm(request.POST or None, request.FILES or None,instance=profile_id)
    #         if form_class.is_valid():
    #             form_class.save()   
    #         context ={
    #             'forms':form_class,
    #         }
            
    #         return render(request,"Employee.html",context)
    #     else:
    #         return render(request,"home-page.html", )

 