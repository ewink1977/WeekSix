from django.urls import path
from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.wall_home, name = 'wall_home'),
    path('addmsg/', views.add_message, name = 'add_message'),
    path('addcomment/<postid>', views.add_comment, name = 'add_comment'),
    path('delete/', views.delete_comment, name = 'delete_comment'),
    path('post/delete/', views.delete_post, name = 'delete_post'),
]