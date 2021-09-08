from django.utils.translation import gettext_lazy as _
from django.db import models

from core.models import TimeStamp, LogicalModel
from user.models import Candidate


class Voice(TimeStamp, LogicalModel):
    name = models.CharField(_("Voice Name"), max_length=90, help_text=_("This is voice name"))
    owner = models.OneToOneField(Candidate, on_delete=models.CASCADE, verbose_name=_("Voice owner"),
                                 help_text=_("This is voice owner"))

    # file field for music

    class Meta:
        verbose_name = _("Voice")
        verbose_name_plural = _("Voices")

    def __str__(self):
        return self.name
