from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm, UsernameField, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser

from django import forms



class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number', ]



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #     }
    # ))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('phone_number', 'date_of_birth', 'avatar')
        fields = ('email', 'phone_number', 'date_of_birth', 'avatar')

    # phone_number = UsernameField(widget=forms.TextInput(
        # attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control flatpickr-basic flatpickr-input active',
            'placeholder': "YYYY-MM-DD",
        }
    ))
    avatar = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'form-control',
        }
    ))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'gender', 'email', 'date_of_birth', 'avatar')
    MY_CHOICES = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=MY_CHOICES,widget=forms.Select(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control'}))
    avatar = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control'}))

class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }
    ))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }
    ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }
    ))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))


class CustomPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }
    ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }
    ))
