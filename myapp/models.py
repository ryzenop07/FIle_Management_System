from django.db import models

# Create your models here.
class adminlogin(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=16)
    create_at=models.TimeField()
    
    
class adddepartment(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    department_name=models.CharField(max_length=225)
    department_code=models.IntegerField()
    department_head=models.CharField(max_length=100)
    status=models.CharField(max_length=20)  
    department_email= models.CharField(max_length=100)
    department_number=models.IntegerField(max_length=12)
    create_at=models.TimeField()
    
    