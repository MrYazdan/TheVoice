from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _

from score.models import ScoreItem as Score


class ScoreList(LoginRequiredMixin, ListView):
    template_name = "score/list.html"

    def get_queryset(self):
        user = self.request.user
        return Score.objects.all() if user.is_superuser \
            else Score.objects.filter(mentor=user) if user.is_mentor \
            else Score.objects.filter(voice__owner=user)


class ScoreDetail(LoginRequiredMixin, DetailView):
    template_name = "score/detail.html"

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs["pk"]

        try:
            return Score.objects.get(pk=pk) if user.is_superuser or (
                    user.is_mentor and Score.objects.get(pk=pk, mentor=user)
            ) or Score.objects.get(pk=pk, voice__owner=user) else None
        except Score.DoesNotExist:
            raise Http404(_('Score not found'))
