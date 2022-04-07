from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.LoginView.as_view(),name='homepage'),
    path('dashboard',views.DashboardView,name='dashboard'),
    path('logout',views.LogoutView,name='logout'),
]