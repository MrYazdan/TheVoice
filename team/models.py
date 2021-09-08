from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models

from core.models import TimeStamp, LogicalModel


class Team(TimeStamp, LogicalModel):

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
