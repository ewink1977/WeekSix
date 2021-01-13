from WallApp.views import wall_home
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

def home(request):
    return render(request, 'html/home.html' )

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('login:home')
        prehash = request.POST['password']
        hash_n_salt = bcrypt.hashpw(prehash.encode(), bcrypt.gensalt(17)).decode()
        newuser = User.objects.create(
            first_name = request.POST['firstname'], 
            last_name = request.POST['lastname'], 
            birthdate = request.POST['birthdate'],
            email = request.POST['email'],
            password = hash_n_salt
        )
        request.session['userid'] = newuser.id
        messages.success(request, f"User { request.POST['email'] } has been created successfully!")
        return redirect('login:success')
    else:
        return redirect('login:home')

def success(request):
    if request.method == 'POST':
        if request.session['userid']:
            context = {
                "userinfo" : User.objects.get(id = request.session['userid'])
            }
            return render(request, 'html/success.html', context)
    else:
        return redirect('login:home')

def logout(request):
    request.session.flush()
    request.session['loggedin'] = False
    return redirect('login:home')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email = request.POST['email_login'])
        if user:
            loggedin_user = user[0]
            print("USER LOCATED")
            if bcrypt.checkpw(request.POST['password_login'].encode(), loggedin_user.password.encode()):
                print("PASSWORD VALIDATED")
                request.session['userid'] = loggedin_user.id
                request.session['loggedin'] = True
                print(request.session['userid'])
                messages.success(request, f"User {loggedin_user.first_name} has logged in!")
                context = {
                    'loggedin_user': loggedin_user
                }
                return redirect('wall:wall_home')
    else:
        return redirect('login:home')