from django.utils.translation import gettext_lazy as _, gettext
from django.core import validators
from django.db import models

from core.models import TimeStamp
from voice.models import Voice
from user.models import Mentor


class ScoreItem(TimeStamp):
    voice = models.ForeignKey(Voice, on_delete=models.CASCADE, verbose_name=_("The voice"),
                              help_text=_("This is voice for this score"))
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, verbose_name=_("Mentor"),
                               help_text=_("This is Mentor Score"))
    score = models.PositiveIntegerField(validators=[
        validators.MinValueValidator(0), validators.MaxValueValidator(100)
    ], verbose_name=_("Score"), help_text=_("This is voice score beetween 0 to 100 of this mentor"))
    description = models.TextField(_("Description"), null=True, blank=True,
                                   help_text=_("This is description for this score"))

    class Meta:
        verbose_name = _("Score Item")
        verbose_name_plural = _("Score Items")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not ScoreItem.objects.filter(mentor=self.mentor, voice=self.voice):
            super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{gettext('score')} : {self.score}"
