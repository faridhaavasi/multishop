from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm
# Create your views here.
'''
def login(request):
    return render(request, 'account/login.html')
'''


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