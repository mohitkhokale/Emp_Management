from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate ,login
from Employee.forms import EmployeeForm


def EmployeeRegisterView(request):

    form_class = EmployeeForm(data = request.POST)
    if form_class.is_valid():
        data = form_class.save()
        username = form_class.cleaned_data.get('username')
        password = form_class.cleaned_data.get('password1')
        userinfo = authenticate(username=username, password=password)
        # login(request, userinfo)
        return redirect('dashboard')
    else:
        context = {
            'forms': form_class,
        }
        return render(request,'Employee.html',context)


#     def post(self,request,pk=None):
#             print(pk)
#             Product_Category = Employee.objects.get(id=pk) 
#             form_class = self.form_class(request.POST,instance=Product_Category)
#             if form_class.is_valid():
#                 form_class.save()
#             print(form_class)
            
#             return render(request,'Employee.html')



 