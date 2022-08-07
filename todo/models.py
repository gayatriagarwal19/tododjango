from pyexpat import model
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
    User = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    ProfilePicture = models.ImageField(upload_to='images', null= True)
    PhoneNumber = models.IntegerField(blank=False)

    
        

 
