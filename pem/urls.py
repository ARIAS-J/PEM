from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    #PEM
    path('', views.welcome, name="welcome"),
    path('home/', views.home, name="home"),
    path('categoria/', views.categoria, name="categoria"),
    path('historial/', views.historial, name="historial"),
    #accounts
    path('register/', views.register, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
]
