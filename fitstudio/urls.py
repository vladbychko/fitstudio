from django.contrib import admin
from django.urls import path
from studio import views     # ← додали

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),   # ← ГОЛОВНИЙ МАРШРУТ
]

