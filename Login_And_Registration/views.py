from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def home(request):
    return render(request, 'html/home.html' )

def register(request):
    errors = User.objects.basic_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='danger')
        return redirect('home')
    return HttpResponse('PASSED')

def login(request):
    pass


