from django.utils.translation import gettext_lazy as _
from core.models import TimeStamp, LogicalModel
from django.db import models


class Team(TimeStamp, LogicalModel):
    name = models.CharField(_("Team Name"), max_length=60, help_text=_("This is team name"))

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name
