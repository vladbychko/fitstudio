from django.contrib import admin
from .models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'specialty')
