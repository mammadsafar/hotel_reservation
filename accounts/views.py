from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .mybackend import PhoneNumberBackend
from . import forms
from .models import CustomUser
from . import helper

class SignUpView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def LogInView(request):
    if request.method == 'POST':
        if 'phone_number' in request.POST:
            phone_number = request.POST.get('phone_number')
            user = CustomUser.objects.get(phone_number=phone_number)
            login(request, user, backend=PhoneNumberBackend)
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'registration/profile.html')

def RegisterView(request):
    form = forms.RegisterForm

    if request.method == 'POST':
        try:
            if 'phone_number' in request.POST:
                phone_number = request.POST.get('phone_number')
                user = CustomUser.objects.get(phone_number=phone_number)
                # send OTP
                # if otp not exist then you can send otp code
                otp = helper.get_random_otp()
                print('OTP: ', otp)
                # helper.send_otp(phone_number, otp)
                # helper.send_otp_soap(phone_number, otp)
                # save OTP
                user.otp = otp
                user.save()
                request.session['user_mobile'] = user.phone_number
                return HttpResponseRedirect(reverse('verify'))

        except CustomUser.DoesNotExist:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # sent OTP
                otp = helper.get_random_otp()
                print('No User OTP: ', otp)
                # helper.send_otp(phone_number, otp)
                # helper.send_otp_soap(phone_number, otp)
                # save OTP
                user.otp = otp
                user.is_active = False
                user.save()
                request.session['user_mobile'] = user.phone_number
                return HttpResponseRedirect(reverse('verify'))

    return render(request, 'registration/register.html', {'form': form})

def verify(request):
    try:
        phone_number = request.session.get('user_mobile')
        user = CustomUser.objects.get(phone_number=phone_number)
        if request.method == 'POST':
            
            # check otp expiration
            if not helper.check_otp_expiration(user.phone_number):
                return HttpResponseRedirect(reverse('register_view'))


            if user.otp != int(request.POST.get('otp')):
                return HttpResponseRedirect(reverse('register_view'))
            
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        return render(request, 'registration/verify.html', {'mobile': phone_number})
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect(reverse('register_view'))

# @login_required(login_url="/accounts/register/")
def ProfileView(request):
    try:
        if not request.user.is_authenticated:
            return reverse('register_view')
        phone_number = request.session.get('user_mobile')
        user = CustomUser.objects.get(phone_number=phone_number)
        form = forms.CustomUserChangeForm
        if request.method == 'POST':

            pass

        return render(request, 'registration/profile.html', {'user': user, 'form':form})
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect(reverse('register_view'))