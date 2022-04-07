from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
# DESIGNATIONS= [
#     ('MANAGER','MANAGER'),
#     ('EMPLOYEE', 'EMPLOYEE')
#     ]

class EmployeeForm(UserCreationForm):

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    deptartment = forms.CharField(max_length=255)
    dob = forms.DateTimeField(label="Date Of Birth", required=True, widget=forms.NumberInput(attrs={'type':'date'}))
    email = forms.EmailField(max_length=255)
    # status = forms.BooleanField()
    mobile = forms.CharField(max_length=255)
    joining_date = forms.DateTimeField(label="Joining Date", required=True, widget=forms.NumberInput(attrs={'type':'date'}))
    # designation = forms.CharField(label='Select Designation: ', widget=forms.Select(choices=DESIGNATIONS))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1', 'password2','dob','mobile','email','is_staff','joining_date')
        # fields = '__all__'
        
        

        