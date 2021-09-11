from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _

from team.models import Team
from user.models import Mentor, Candidate


class TeamList(LoginRequiredMixin, ListView):
    template_name = "team/list.html"

    def get_queryset(self):
        user = self.request.user
        return Team.objects.all() if user.is_superuser else Mentor.objects.get(user_ptr_id=user.id).teams.all() \
            if Mentor.objects.filter(user_ptr_id=user.id) else Candidate.objects.get(user_ptr_id=user.id).team


class TeamDetail(LoginRequiredMixin, DetailView):
    template_name = "team/detail.html"

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs["pk"]

        try:
            return Team.objects.get(pk=pk) if user.is_superuser or (
                    Mentor.objects.filter(user_ptr_id=user.id) and Team.objects.get(pk=pk) in
                    Mentor.objects.get(user_ptr_id=user.id).teams.all()
            ) or Candidate.objects.get(user_ptr_id=user.id).team.id == pk else None
        except Team.DoesNotExist:
            raise Http404(_('Team not found'))
