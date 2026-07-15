from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime


# Create your views here.
def home(request):
    return render(request,'user/home.html')

def Adminlogin(request):
    return render(request,'admin/adminlogin.html')

def loginsave(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=adminlogin.objects.filter(username=username,password=password).first()
        if user:
            request.session['adminid']=username
            return redirect('dashboard')
        else:
            return redirect('adminlogin')

def dashboard(request):
    return render(request,'admin/dashboard.html')

def adminlayout(request):
    return render(request,'admin/adminlayout.html')

def logout(request):
    request.session.flush()
    return redirect('adminlogin')

def adddep(request):
    return render(request,'admin/adddep.html')

def dep_save(request):
    if request.method=="POST":
        department_name=request.POST.get('department_name')
        department_code=request.POST.get('department_code')
        department_head=request.POST.get('department_head')
        status=request.POST.get('status')
        department_email=request.POST.get('department_email')
        department_number=request.POST.get('department_number')
        create_at=datetime.now()
        ab=adddepartment(department_name=department_name,department_code=department_code,department_head=department_head,status=status,department_email=department_email,department_number=department_number,create_at=create_at)
        ab.save()
        messages.success(request,'Add Deparment Succeeesfully')
        return redirect('adddep')
        
def depshow(request):
    ab=adddepartment.objects.all()
    return render(request,'admin/depshow.html',{'ab':ab})






