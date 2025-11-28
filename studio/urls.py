from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("trainers/", views.trainers, name="trainers"),
    path("programs/", views.programs, name="programs"),
    path("prices/", views.prices, name="prices"),
    path("booking/", views.booking, name="booking"),
]




