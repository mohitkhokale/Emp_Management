from django.urls import path
from . import views

urlpatterns = [
    path('task',views.TaskView.as_view(),name="task"),
    path('update_task/<int:task_id>',views.update_task,name="update_task"),
#   path('dashboard',views.DashboardView,name='dashboard'),

]
