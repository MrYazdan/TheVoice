from django.contrib import admin
from .models import *


@admin.register(Voice)
class VoiceAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'create_time', 'is_active']
    list_editable = ['is_active']
