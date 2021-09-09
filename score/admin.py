from django.contrib import admin
from .models import *


@admin.register(ScoreItem)
class ScoreItemAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'voice', 'mentor', 'score']