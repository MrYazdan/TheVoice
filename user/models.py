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

    def create_mentor(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        extra_fields['is_mentor'] = True
        return super().create_user(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    age = models.PositiveIntegerField(null=True, blank=True, validators=[validators.MaxValueValidator(99)])
    phone = models.CharField(max_length=11, unique=True, validators=[
        validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message=_("Phone number must be entered in the true IR (iran) format."),
                                  code=_('invalid IR phone number'))
    ])
    is_mentor = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone


class Candidate(TimeStamp, LogicalModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Candidate user"),
                                help_text=_("This is Candidate user"))

    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Candidates team"),
                             help_text=_("This is Candidates team"))

    class Meta:
        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidates")

    def __str__(self):
        return f"{self.user.get_full_name()}"


class Mentor(TimeStamp, LogicalModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Mentor user"),
                                help_text=_("This is Mentor user"))

    teams = models.ManyToManyField(Team, verbose_name=_("Candidates team"),
                                   help_text=_("This is Candidates team"), related_name="teams")

    class Meta:
        verbose_name = _("Mentor")
        verbose_name_plural = _("Mentors")

    def __str__(self):
        return f"{self.user.get_full_name()}"
