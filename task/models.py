import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
     
class Task(models.Model):
        
    status= [
    ('OPEN','OPEN'),
    ('IN-PROGRESS', 'IN-PROGRESS'),
    ('COMPLETED', 'COMPLETED')
    ]
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name="emp")
    title = models.CharField(max_length=255)
    task_status = models.CharField(max_length=50,choices=status,default='open')
    created_at = models.DateTimeField()
    date_of_submit = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

  
# class assignTask(models.Model):

#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     admin=models.ForeignKey(User, on_delete=models.CASCADE)
  
#     def write(self):
#         return ",".join([str(x) for x in self.user.all()])
 