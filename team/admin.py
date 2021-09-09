from django.contrib import admin
from .models import *


@admin.register(Team)
class TeamAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'create_time', 'is_active']
    list_editable = ['is_active']