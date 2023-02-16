from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, UpdateView
from .forms import LoginForm, RegisterForm, CheckOtpForm, RegisterFinalForm, Edit_Form
import ghasedakpack
from random import randint
from .models import User, Otp
from django.utils.crypto import get_random_string
# Create your views here.
'''
def login(request):
    return render(request, 'account/login.html')
'''

sms = ghasedakpack.Ghasedak("Your APIKEY")
class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'user is not valid')

        else:
            form.add_error('phone', 'invalid data')

        return render(request, 'account/login.html', {'form': form})


class RegisterUser(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randomcode = randint(1000, 9999)
            print(randomcode)
            token = get_random_string(length=20)

            sms.verification({'receptor': cd['phone'], 'type': '1', 'template': 'randcodemoltishop', 'param1': randomcode})
            Otp.objects.create(phone=cd['phone'], randomcode=randomcode, token=token)

            return redirect(reverse('account:checkotp') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid phone')

        return render(request, 'account/register.html', {'form': form})

class CheckOtp(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/checkotp.html', {'form': form})
    def post(self, request):
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            token = request.GET.get('token')
            cd = form.cleaned_data
            randomcode = Otp.objects.filter(randomcode=cd['code'])
            if randomcode:
                return redirect(reverse('account:registerfinal') + f'?token={token}')
        else:
            form.add_error('code', 'invalid code')
        return render(request, 'account/checkotp.html', {'form': form})

class RegisterFinal(View):
    def get(self, request):
        form =RegisterFinalForm()
        return render(request, 'account/registerfinal.html', {'form': form})
    def post(self, request):
        form = RegisterFinalForm(request.POST)
        if form.is_valid():
            token = request.GET.get('token')
            cd = form.cleaned_data
            obj = Otp.objects.get(token=token)
            phone_number = obj.phone
            user = User.objects.create(phone_number=phone_number, password=cd['password'])
            login(request, user)

            return redirect('home:home')
        return render(request, 'account/registerfinal.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')

class Edit_profile(UpdateView):
    model = User
    fields = ['email', 'phone_number', 'full_name']
    #form_class = Edit_Form()
    template_name = 'account/edit_profile.html'
    success_url = '/'






