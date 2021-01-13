from django.shortcuts import render, redirect, HttpResponse
from Login_And_Registration.models import User, WallPost, Comments
from django.contrib import messages

def wall_home(request):
    if request.session['loggedin'] == False:
        messages.error(request, f"You must be logged in to post to the wall.", extra_tags='danger')
        return redirect('login:home')
    context = {
        'wallposts': WallPost.objects.all(),
        'comments': Comments.objects.all(),
        'loggedinuser': User.objects.get(id = request.session['userid'])
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
    else:
        return redirect('wall:wall_home')

def add_comment(request, postid):
    if request.method == 'POST':
        posting_user = User.objects.get(id = request.session['userid'])
        wall_post = WallPost.objects.get(id = postid)
        new_comment = Comments.objects.create(
            comment = request.POST['comment'],
            user = posting_user,
            message = wall_post,
        )
        return redirect('wall:wall_home')
    else:
        return redirect('wall:wall_home')

def delete_post(request):
    if request.method == 'POST':
        post_to_kill = WallPost.objects.get(id = request.POST['commentid'])
        post_to_kill.delete()
        return redirect('wall:wall_home')
    else:
        return redirect('wall:wall_home')

def delete_comment(request):
    if request.method == 'POST':
        comment_to_kill = Comments.objects.get(id = request.POST['commentid'])
        comment_to_kill.delete()
        return redirect('wall:wall_home')
    else:
        return redirect('wall:wall_home')