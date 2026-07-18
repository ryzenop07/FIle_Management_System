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
            messages.error(request,'Invalid username or password')
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




def empadd(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    else:
        if request.method == "POST":
            
            
            Empadd.objects.create(
                name=request.POST.get('name'),
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                mobile=request.POST.get('mobile'),
                emp_id=request.POST.get('emp_id'),
                department=request.POST.get('department'),
                designation=request.POST.get('designation'),
                role=request.POST.get('role'),
                status=request.POST.get('status'),
                password=request.POST.get('password'),
                photo=request.FILES.get('photo'),
                address=request.POST.get('address'),
            )
            return redirect('home')
    return render(request, 'admin/empadd.html')

def empshow(request):
    ab=Empadd.objects.all()
    return render(request,'admin/empshow.html',{'ab':ab})


def userdashboard(request):
    return render(request,'user/userdashboard.html')


def recievedfile(request):
    return render(request, 'admin/recievedfile.html')

def Userlogin(request):
    return render(request,'user/userlogin.html')


def userlogcode(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=Empadd.objects.filter(username=username,password=password).first()
        if user:       
            if user.role=="User" and user.status=="Active":
                request.session['userid']=username
                return redirect('home')
            else:
                return redirect('userdashboard')
            
    return redirect('userlogin')


def userlayout(request):
    return render(request, 'user/userlayout.html')

def createfile(request):
    userid=request.session.get('userid')
    dp=adddepartment.objects.all()
    em=Empadd.objects.all()
    
    if request.method=="POST":
        Fileupload.objects.create(
            file_no=request.POST.get('file_no'),
            subject=request.POST.get('subject'),
            create_user=userid,
            priority=request.POST.get('priority'),
            department=request.POST.get('department'),
            current_user=request.POST.get('current_user'),
            file=request.FILES.get('file'),
            description=request.POST.get('description'),
            create_at=datetime.now(),
            status="Forwarded"
        )
        return redirect('createfile')
    
    con={
        'dp':dp,
        'em':em
    }
    return render(request,'admin/createfile.html',con)

