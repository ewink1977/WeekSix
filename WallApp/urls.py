from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_home, name = 'wall_home'),
]