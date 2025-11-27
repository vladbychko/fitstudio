from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trainers/', views.trainers, name='trainers'),
    path('prices/', views.prices, name='prices'),
    path('programs/', views.programs, name='programs'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
]



