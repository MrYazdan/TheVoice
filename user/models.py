from django.contrib.auth.models import UserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models

from core.models import TimeStamp, LogicalModel
from team.models import Team


class CustomUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

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

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    objects = CustomUserManager()


class Candidate(User):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, verbose_name=_("Candidates team"), null=True, blank=True,
                             help_text=_("This is Candidates team"))

    class Meta:
        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidates")

    def __str__(self):
        return f"{self.phone} {self.get_full_name()}"


class Mentor(User):
    teams = models.ManyToManyField(Team, verbose_name=_("Candidates team"), null=True, blank=True,
                                   help_text=_("This is Candidates team"), related_name="teams")

    class Meta:
        verbose_name = _("Mentor")
        verbose_name_plural = _("Mentors")

    def __str__(self):
        return f"{self.phone} {self.get_full_name()}"
