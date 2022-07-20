from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from argon2 import PasswordHasther
from accounts.forms import RegisterForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form}
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(
                user_id = register_form.user_id,
                user_pwd = register_form.user_pwd,
                user_name = register_form.user_name,
                user_phone = register_form.user_phone
            )
            user.save()
            return redirect('login/')
        else:
            context['forms'] = register_form
            if register_form.erors:
                for value in register_form.erros.values():
                    context['error'] = value
        return render(request, 'accounts/register.html', context)
    
    else:
        return render(request, 'accounts/register.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')