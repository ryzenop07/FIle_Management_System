from django.db import models

# Create your models here.
class login(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=16)
    role=models.CharField(max_length=50)
   
    
    
class adddepartment(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    department_name=models.CharField(max_length=225)
    department_code=models.IntegerField()
    department_head=models.CharField(max_length=100)
    status=models.CharField(max_length=20)  
    department_email= models.CharField(max_length=100)
    department_number=models.IntegerField(max_length=12)
    create_at=models.DateTimeField(auto_now_add=True)
    
class Empadd(models.Model):
    name=models.CharField(max_length=225)
    username=models.CharField(max_length=225)
    email=models.EmailField(max_length=225)
    mobile=models.IntegerField()
    emp_id=models.IntegerField(primary_key=True,auto_created=True)
    department=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)
    role=models.CharField(max_length=200)
    status=models.CharField(max_length=20)  
    password=models.CharField(max_length=16)
    photo=models.ImageField(upload_to="profile")
    address=models.CharField(max_length=500)
    
class Fileupload(models.Model):
    file_no=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)
    priority=models.CharField(max_length=50)
    create_user=models.CharField(max_length=100)
    department=models.CharField(max_length=250)
    current_user=models.CharField(max_length=100)
    file=models.FileField(upload_to="upload_file")
    description=models.CharField(max_length=1000)
    status=models.CharField(max_length=200)
    create_at=models.TimeField()

class File_history(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    File_no=models.CharField(max_length=100)
    current_user=models.CharField(max_length=225)
    forwarded_user=models.CharField(max_length=225)
    action=models.CharField(max_length=225)
    remark=models.CharField(max)
    create_at=models.DateTimeField()
    
    
    
    
    
    