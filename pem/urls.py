from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from . import views




urlpatterns = [
    #PEM
    path('home/', views.home, name="home"),
    path('categoria/', views.categoria, name="categoria"),
    path('historial/', views.historial, name="historial"),
    #accounts
    path('register/', views.register, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
]
