from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.views.decorators.cache import cache_control


# Create your views here.
def home(request):
    return render(request,'user/home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Adminlogin(request):
    return render(request,'admin/adminlogin.html')

def loginsave(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=login.objects.filter(username=username,password=password).first()
        if user:
            request.session['adminid']=username
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('adminlogin')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request,'admin/dashboard.html')

def adminlayout(request):
    return render(request,'admin/adminlayout.html')

def logout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
    
    return redirect('adminlogin')

def userlogout(request):
    if 'userid' in request.session:
        del request.session['userid']
    
    return redirect('userlogin')

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
        create_at=timezone.now
        
        av=adddepartment.objects.filter(department_name=department_name,department_code=department_code,department_email=department_email)
        if av.exists():
            messages.error(request, "This Department already exists")
            return redirect('adddep')
        else:
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
            username=request.POST.get('username')
            empid=request.POST.get('empid')
            password=request.POST.get('password')
            sv=login(username=username, password=password)
            sv.save()
            av=Empadd.objects.filter(username=username, emp_id=empid)
            if av.exists():
                messages.error(request, "This Employee already exists")
                return redirect('empadd')
            else:
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
                messages.success(request, 'Add Employee Succeeesfully')
                
                
            return redirect('empadd')
        return render(request, 'admin/empadd.html')

def empshow(request):
    ab=Empadd.objects.all()
    return render(request,'admin/empshow.html',{'ab':ab})


def userdashboard(request):
    return render(request,'user/userdashboard.html')



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
                return redirect('userdashboard')
            else:
                
                return redirect('home')
            
    return redirect('userlogin')


def userlayout(request):
    return render(request, 'user/userlayout.html')

def createfile(request):
    userid=request.session.get('adminid')
    dp=adddepartment.objects.all()
    em=login.objects.all()
    
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
        messages.success(request,"File Created Succesfully")
        return redirect('createfile')
    
    con={
        'dp':dp,
        'em':em
    }
    return render(request,'admin/createfile.html',con)

def recievedfile(request):
    sid=request.session.get('adminid')
    ab=Fileupload.objects.filter(create_user=sid)
    return render(request, 'admin/recievedfile.html',{'ab':ab})




def us_createfile(request):
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
        return redirect('us_createfile')
    
    con={
        'dp':dp,
        'em':em
    }
    return render(request,'user/us_createfile.html',con)


    
def us_recievedfile(request):
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(current_user=sid)
    return render(request, 'user/us_recievedfile.html',{'ab':ab})



def sentfile(request):
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(create_user=sid)
    return render(request, 'admin/sentfile.html', {'ab':ab})

def allfile(request):
    sid=request.session.get('adminid')
    ab=Fileupload.objects.filter(
        Q(create_user=sid) | Q(current_user=sid)
    )
    return render(request,'admin/allfile.html',{'ab':ab})

def us_sentfile(request):
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(create_user=sid)
    return render(request, 'user/us_sentfile.html', {'ab':ab})

def us_allfile(request):
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(
        Q(create_user=sid) | Q(current_user=sid)
    )
    return render(request,'user/us_allfile.html',{'ab':ab})

def details_file(request,file_no):
    ur=login.objects.all()
    ab=Fileupload.objects.get(file_no=file_no)
    context={
        'ab':ab,
        'ur':ur
    }
    return render(request,'user/details_file.html',context)