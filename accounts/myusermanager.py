from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **other_fields):
        if not phone_number:
            raise ValueError("Phone number is required...!")
        user = self.model(phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, phone_number, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("SuperUser most have is_staff=True...!")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("SuperUser most have is_superuser=True...!")
        return self.create_user(phone_number, password, **other_fields)
