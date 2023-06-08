from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from . import forms

urlpatterns = [

    path('register/', views.RegisterView, name='register_view'),
    path('verify/', views.verify, name='verify'),

    path('user/', views.ProfileView, name='profile'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        "password_change/", PasswordChangeView.as_view(
            form_class=forms.UserChangePasswordForm
        ), name="password_change"
    ),
    path("password_reset/", PasswordResetView.as_view(
        form_class=forms.CustomPasswordResetForm
    ), name="password_reset"),

    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        form_class=forms.CustomPasswordResetConfirmForm
    ), name="password_reset_confirm", ),

]
