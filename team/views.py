from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _

from team.models import Team
from user.models import Mentor, Candidate


class TeamList(LoginRequiredMixin, ListView):
    template_name = "team/list.html"

    def get_queryset(self):
        user = self.request.user
        return Team.objects.all() if user.is_superuser else Mentor.teams.all() if user.is_mentor else Candidate.team


class TeamDetail(LoginRequiredMixin, DetailView):
    template_name = "team/detail.html"

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs["pk"]

        try:
            return Team.objects.get(pk=pk) if user.is_superuser or (
                    user.is_mentor and Team.objects.get(pk=pk) in Mentor.objects.get(user=user).teams.all()
            ) or Candidate.objects.get(user=user).team.id == pk else None
        except Exception:
            raise Http404(_('Team not found'))
