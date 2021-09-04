from django.db import models

# Create your models here.

# class regi(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.CharField(max_length=30)
#     password=models.CharField(max_length=12)
#     contact=models.IntegerField()
#     status=models.CharField(max_length=10)
# class logi(models.Model):
#     username2=models.CharField(max_length=50)
#     password2=models.CharField(max_length=50)
#     status=models.CharField(max_length=10)

class regi(models.Model):
    username=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=10,null=True)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="")

class logi(models.Model):
    username2=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="")