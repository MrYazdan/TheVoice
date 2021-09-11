from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _

from score.models import ScoreItem as Score
from user.models import Mentor


class ScoreList(LoginRequiredMixin, ListView):
    template_name = "score/list.html"

    def get_queryset(self):
        user = self.request.user
        return Score.objects.all() if user.is_superuser \
            else Score.objects.filter(mentor__user_ptr_id=user.id) if Mentor.objects.filter(user_ptr_id=user.id) \
            else Score.objects.filter(voice__owner_user_ptr_id=user.id)


class ScoreDetail(LoginRequiredMixin, DetailView):
    template_name = "score/detail.html"

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs["pk"]

        try:
            return Score.objects.get(pk=pk) if user.is_superuser or (
                    Mentor.objects.filter(user_ptr_id=user.id) and Score.objects.get(pk=pk, mentor__user_ptr_id=user.id)
            ) or Score.objects.get(pk=pk, voice__owner_user_ptr_id=user.id) else None
        except Score.DoesNotExist:
            raise Http404(_('Score not found'))
