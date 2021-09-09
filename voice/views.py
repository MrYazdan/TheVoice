from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.http import Http404

from user.models import Mentor
from voice.models import Voice


class VoiceList(LoginRequiredMixin, ListView):
    template_name = "voice/list.html"

    def get_queryset(self):
        user = self.request.user
        return Voice.objects.all() if user.is_superuser \
            else Voice.objects.filter(owner__team__in=Mentor.objects.get(user=user).teams.all()) if user.is_mentor \
            else Voice.objects.filter(owner=user)


class VoiceDetail(LoginRequiredMixin, DetailView):
    template_name = "voice/detail.html"

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs["pk"]

        try:
            return Voice.objects.get(pk=pk) if user.is_superuser or (
                    user.is_mentor and Voice.objects.get(pk=pk, owner__team__in=Mentor.objects.get(user=user).teams.all())
            ) or Voice.objects.get(pk=pk, owner=user) else None
        except Voice.DoesNotExist:
            raise Http404(_('Voice not found'))
