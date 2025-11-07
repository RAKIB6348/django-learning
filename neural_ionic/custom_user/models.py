from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]

    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    UserType = models.CharField(choices=USER_TYPES, max_length=100)
    display_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    gender = models.CharField(choices=GENDER, max_length=100)
    