from cProfile import Profile
from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
# from tkinter import CASCADE
from django.db.models.deletion import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    title= models.CharField(max_length=50)
    description = models.TextField(max_length=200)  
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add= True , null = True)
    status = models.CharField(max_length=2 , choices= status_choices, null = True)


    def __str__(self):
        return self.title


class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    ProfilePhoto = models.FileField(upload_to = 'images' ,null = True)
    PhoneNumber = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.user}'

 
