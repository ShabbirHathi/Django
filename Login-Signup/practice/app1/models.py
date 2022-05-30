from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class User(AbstractUser):
     
     username=models.CharField(max_length=30,unique=True)
     email=models.EmailField()
    #  password=models.CharField(max_length=20)

     def __str__(self):
         return self.username
     
