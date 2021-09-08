from django.contrib.auth.models import UserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models


class CustomUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_mentor(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        extra_fields['is_mentor'] = True
        return super().create_user(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    phone = models.CharField(max_length=11, unique=True, validators=[
        validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message=_("Phone number must be entered in the true IR (iran) format."),
                                  code=_('invalid IR phone number'))
    ])
    is_mentor = models.BooleanField(default=False)

    objects = CustomUserManager()

