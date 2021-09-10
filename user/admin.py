from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(User)
class UesrAdminModel(BaseUserAdmin):
    list_display = ['__str__', 'is_superuser', 'is_active']
    list_editable = ['is_active']
    readonly_fields = ['password']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Candidate)
class CandidateAdminModel(BaseUserAdmin):
    list_display = ['__str__', 'team', 'is_active']
    list_editable = ['is_active']
    readonly_fields = ['is_staff', 'is_superuser', 'date_joined', 'is_active', 'user_permissions', 'groups', 'username',
                       'last_login', 'phone']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Mentor)
class MentorAdminModel(BaseUserAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    list_horizontal = ['teams']
    readonly_fields = ['is_staff', 'is_superuser', 'date_joined', 'is_active', 'user_permissions', 'groups', 'username',
                       'last_login', 'phone']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
