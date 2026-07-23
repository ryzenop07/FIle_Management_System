from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.conf import settings
import re

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
            if user.role=="Admin":
                request.session['adminid']=username
                return redirect('dashboard')
            else:
                messages.success(request,'Enter Your Admin Username And Password')
                return redirect('adminlogin')
        else:
            messages.success(request, 'Invalid Username Or Password')
            return redirect('adminlogin')
      

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
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
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    return render(request,'admin/adddep.html')

def dep_save(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
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
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    ab=adddepartment.objects.all()
    return render(request,'admin/depshow.html',{'ab':ab})




def empadd(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            empid=request.POST.get('empid')
            name=request.POST.get('name')
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
                message = f"""
                Dear {name},

                Greetings from Green Gas Limited (GGL).

                Your account has been successfully created for the GGL File Tracking System.

                You can log in using the following credentials:

                --------------------------------------------------------
                User ID / Email : {username}
                Password        : {password}
                --------------------------------------------------------

                Login Instructions:
                1. Open the GGL File Tracking System.
                2. Enter your User ID and Password.
                3. Change your password after your first login (if applicable).
                4. Start managing and tracking your assigned files.

                Important:
                • Keep your login credentials confidential.
                • Do not share your password with anyone.
                • If you forget your password or face any login issues, please contact the System Administrator.

                Thank you for using the GGL File Tracking System.

                Regards,

                System Administrator
                GGL File Tracking System
                Green Gas Limited (GGL)
                """

            send_mail(
                    "GGL File Tracking System - Login Credentials",
                    message,
                    settings.EMAIL_HOST_USER,
                    [username],
                    fail_silently=False
                )
                
                
            return redirect('empadd')
        return render(request, 'admin/empadd.html')

def empshow(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    ab=Empadd.objects.all()
    return render(request,'admin/empshow.html',{'ab':ab})


def userdashboard(request):
    if 'userid' not in request.session:
        return redirect('userlogin')
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createfile(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    else:

        adminid = request.session.get('adminid')
        dp = adddepartment.objects.all()
        em = login.objects.all()

        if request.method == "POST":

            # Auto Generate Unique File Number
            last = Fileupload.objects.order_by('-file_no').first()

            if last and last.file_no:
                num = int(re.sub(r'\D', '', last.file_no))
            else:
                num = 0

            while True:
                num += 1
                file_no = f"FIL{num:03d}"   # FIL001, FIL002, FIL003...

                # Check Duplicate
                if not Fileupload.objects.filter(file_no=file_no).exists():
                    break

            current_user = request.POST.get('current_user')
            description = request.POST.get('description')

            Fileupload.objects.create(
                file_no=file_no,
                subject=request.POST.get('subject'),
                create_user=adminid,
                priority=request.POST.get('priority'),
                department=request.POST.get('department'),
                current_user=current_user,
                file=request.FILES.get('file'),
                description=description,
                create_at=datetime.now(),
                status="Forwarded"
            )

            File_history.objects.create(
                File_no=file_no,
                current_user=adminid,
                forwarded_user=current_user,
                action="Forwarded",
                remark=description,
                create_at=timezone.now()
            )

            messages.success(request, "File Create Successfully")
            return redirect('createfile')

        con = {
            'dp': dp,
            'em': em
        }

        return render(request,'admin/createfile.html',con)

def recievedfile(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    sid=request.session.get('adminid')
    ab=Fileupload.objects.filter(current_user=sid)
    return render(request, 'admin/recievedfile.html',{'ab':ab})




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def us_createfile(request):
    if 'userid' not in request.session:
        return redirect('userlogin')
    else:

        userid = request.session.get('userid')
        dp = adddepartment.objects.all()
        em = login.objects.all()

        if request.method == "POST":

            # Auto Generate Unique File Number
            last = Fileupload.objects.order_by('-file_no').first()

            if last and last.file_no:
                num = int(re.sub(r'\D', '', last.file_no))
            else:
                num = 0

            while True:
                num += 1
                file_no = f"FIL{num:03d}"   # FIL001, FIL002, FIL003...

                # Check Duplicate
                if not Fileupload.objects.filter(file_no=file_no).exists():
                    break
            current_user=request.POST.get('current_user')
            description=request.POST.get('description')
            status="Forwarded"
            create_at=datetime.now()
            fhs=File_history(File_no=file_no,current_user=userid,forwarded_user=current_user,remark=description,action=status,create_at=create_at)

            fhs.save()

        

            Fileupload.objects.create(
                file_no=file_no,
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

            messages.success(request, "File Create Successfully")
            return redirect('us_createfile')


        con = {
            'dp': dp,
            'em': em
        }

        return render(request,'user/us_createfile.html',con)



    
def us_recievedfile(request):
    if 'userid' not in request.session:
        return redirect('userlogin')
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(current_user=sid)
    return render(request, 'user/us_recievedfile.html',{'ab':ab})



def sentfile(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    sid=request.session.get('adminid')
    ab=Fileupload.objects.filter(create_user=sid)
    return render(request,'admin/sentfile.html',{'ab':ab})

def allfile(request):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    sid=request.session.get('adminid')
    ab=Fileupload.objects.filter(
        Q(create_user=sid) | Q(current_user=sid)
    )
    return render(request,'admin/allfile.html',{'ab':ab})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def ad_details_file(request,file_no):
    if 'adminid' not in request.session:
        return redirect('adminlogin')
    sn=request.session.get('adminid')
    ur=login.objects.all()
    ab=Fileupload.objects.get(file_no=file_no)
    fileh=File_history.objects.filter(File_no=file_no)
    if request.method=="POST":
        current_user=request.POST.get('current_user')
        action=request.POST.get('action')
        forwarded_user=request.POST.get('forwarded_user')
        remark=request.POST.get('remark')
        create_at=timezone.now()
        ab.current_user=forwarded_user
        ab.status=action
        ab.save()
        fh=File_history(File_no=ab.file_no,current_user=sn,action=action,forwarded_user=forwarded_user,remark=remark,create_at=create_at)
        fh.save()
        return redirect('recievedfile')
        
    context={
        'ab':ab,
        'ur':ur,
        'fileh':fileh
    }
    return render(request,'admin/ad_details_file.html',context)












def us_sentfile(request):
    if 'userid' not in request.session:
        return redirect('userlogin')
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(create_user=sid)
    return render(request, 'user/us_sentfile.html', {'ab':ab})

def us_allfile(request):
    if 'userid' not in request.session:
        return redirect('userlogin')
    sid=request.session.get('userid')
    ab=Fileupload.objects.filter(
        Q(create_user=sid) | Q(current_user=sid)
    )
    return render(request,'user/us_allfile.html',{'ab':ab})

def details_file(request,file_no):
    if 'userid' not in request.session:
        return redirect('userlogin')
    sn=request.session.get('userid')
    ur=login.objects.all()
    ab=Fileupload.objects.get(file_no=file_no)
    fileh=File_history.objects.filter(File_no=file_no)
    if request.method=="POST":
        current_user=request.POST.get('current_user')
        action=request.POST.get('action')
        forwarded_user=request.POST.get('forwarded_user')
        remark=request.POST.get('remark')
        create_at=timezone.now()
        ab.current_user=forwarded_user
        ab.status=action
        ab.save()
        fh=File_history(File_no=ab.file_no,current_user=sn,action=action,forwarded_user=forwarded_user,remark=remark,create_at=create_at)
        fh.save()
        return redirect('us_recievedfile')
        
    context={
        'ab':ab,
        'ur':ur,
        'fileh':fileh
    }
    return render(request,'user/details_file.html',context)


        