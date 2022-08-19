from django.db import models
from django .contrib.auth .models import User
import random
# Create your models here.
class Employee(models.Model):
    about=models.CharField(max_length=120)
    designation = models.CharField(max_length=80)
    company= models.CharField(max_length=120,null=True)
    yearofexperience = models.PositiveIntegerField(null=True)
    description=models.CharField(max_length=150,null=True)
    image= models.ImageField(upload_to='profilepics', null=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True)
    options = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )
    gender = models.CharField(max_length=12, choices=options, default='male')
    address=models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')

