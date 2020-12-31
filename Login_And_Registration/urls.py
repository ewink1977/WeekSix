from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('register/', views.register, name = "register"),
    path('login/', views.login, name = "login"),
    path('success/', views.success, name = "success"),
    path('logout/', views.logout, name = "logout"),
]