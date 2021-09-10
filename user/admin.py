from django.contrib import admin
from .models import *


@admin.register(User)
class UesrAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'is_superuser', 'is_active']
    list_editable = ['is_active']
    readonly_fields = ['password']


@admin.register(Candidate)
class CandidateAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'team', 'is_active']
    list_editable = ['is_active']
    readonly_fields = ['is_staff', 'is_superuser', 'date_joined', 'is_active', 'user_permissions', 'groups', 'username',
                       'last_login']


@admin.register(Mentor)
class MentorAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    list_horizontal = ['teams']
    readonly_fields = ['is_staff', 'is_superuser', 'date_joined', 'is_active', 'user_permissions', 'groups', 'username',
                       'last_login']
