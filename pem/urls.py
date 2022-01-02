from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('categoria/', views.categoria),
    path('historial/', views.historial)
]
