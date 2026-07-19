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
    path('depshow',depshow,name='depshow'),
    path('userlogin',Userlogin,name='userlogin'),
    path('userlogcode',userlogcode,name='userlogcode'),
    path('empadd',empadd,name='empadd'),
    path('empshow',empshow,name='empshow'),
    path('userdashboard', userdashboard, name='userdashboard'),
    path('userlayout',userlayout,name='userlayout'),
    path('createfile', createfile, name='createfile'),
    path('recievedfile', recievedfile, name='recievedfile'),
    path('us_createfile', us_createfile, name='us_createfile'),
    path('us_recievedfile', us_recievedfile, name='us_recievedfile'),
]
