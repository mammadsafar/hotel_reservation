from typing import Any, Optional
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import CustomUser


class PhoneNumberBackend(ModelBackend):
    
    def authenticate(self, request, username= None, password= None, **kwargs):
        phone_number = kwargs['phone_number']
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            pass
