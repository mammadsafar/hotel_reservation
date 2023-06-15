from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from accounts.myusermanager import MyUserManager
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class CustomUser(AbstractUser):
    MY_CHOICES = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )

    username = None
    phone_number = models.CharField(max_length=11, unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='/media/avatars/default.png')
    gender = models.CharField(max_length=20, choices=MY_CHOICES)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []

    backend = 'accounts.mybackend.PhoneNumberBackend'