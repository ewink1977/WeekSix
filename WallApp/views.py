from django.shortcuts import render, redirect, HttpResponse
from Login_And_Registration.models import User, WallPost, Comments
from django.contrib import messages

def wall_home(request):
    if request.session['loggedin'] == False:
        messages.error(request, f"You must be logged in to access the wall.", extra_tags='danger')
        return redirect('login:home')
    else:
        context = {
            'wallposts': WallPost.objects.all(),
            'comments': Comments.objects.all(),
        }
        return render(request, 'wallapp/wall.html', context)
        

def add_message(request):
    if request.method == 'POST':
        posting_user = User.objects.get(id = request.session['userid'])
        new_message = WallPost.objects.create(
            message = request.POST['message'],
            user = posting_user,
        )
        return redirect('wall:wall_home')
