from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models

from core.models import TimeStamp
from user.models import Mentor


class ScoreItem(TimeStamp):
    # voice = models.ForeignKey()
    mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE, verbose_name=_("Mentor Score")
                                  , help_text=_("This is Mentor Score"))
    score = models.PositiveIntegerField(validators=[
        validators.MinValueValidator(0), validators.MaxValueValidator(100)
    ])
    description = models.TextField(_("Description"), null=True, blank=True)

    class Meta:
        verbose_name = _("Score Item")
        verbose_name_plural = _("Score Items")

    def __str__(self):
        return f"{self.mentor.user.get_full_name()} - score : {self.score}"
