from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('adminlogin',Adminlogin,name='adminlogin'),
    path('loginsave',loginsave,name="loginsave"),
    path('dashboard',dashboard,name="dashboard"),
    path('adminlayout',adminlayout,name='adminlayout'),
    path('logout',logout,name='logout'),
    path('adddep',adddep,name='adddep'),
    path('dep_save',dep_save,name='dep_save'),
    path('depshow',depshow,name='depshow')
    
   
]
