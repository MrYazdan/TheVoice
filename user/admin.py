from django.contrib import admin
from .models import *


@admin.register(User)
class UesrAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'is_mentor', 'is_superuser', 'is_active']
    list_editable = ['is_active']
    readonly_fields = ['password']


@admin.register(Candidate)
class CandidateAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'is_active', 'create_time']
    list_editable = ['is_active']


@admin.register(Mentor)
class MentorAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'is_active', 'create_time']
    list_editable = ['is_active']
    list_horizontal = ['teams']
