from django.urls import path
from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.wall_home, name = 'wall_home'),
    path('addmsg/', views.add_message, name = 'add_message'),
]