from django.shortcuts import render, redirect, HttpResponse
from Login_And_Registration.models import User, Messages, Comments
from django.contrib import messages

def wall_home(request):
    if request.session['loggedin'] == False:
        messages.error(request, f"You must be logged in to access the wall.", extra_tags='danger')
        return redirect('login:home')
    else:
        return render(request, 'wallapp/wall.html')
        

def add_message(request, userid):
    pass

