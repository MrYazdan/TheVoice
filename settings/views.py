from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from team.models import Team
from user.models import Candidate, Mentor
from voice.models import Voice


class Handler(LoginRequiredMixin, View):

    def get(self, request):
        # check user type (candidate - mentor - admin):
        user = self.request.user
        # annonymous user -> redirect to login page
        # admin user :
        if user.is_superuser:
            context = {
                "teams": Team.objects.all(),
                "mentors": Mentor.objects.all(),
                "candidates": Candidate.objects.all(),
            }

            return render(self.request, "user/admin.html", context)

        # mentor user :
        elif Mentor.objects.filter(user_ptr_id=user.id):
            mentor = Mentor.objects.get(user_ptr_id=user.id)
            context = {
                "teams": mentor.teams.all(),
                "candidates": Candidate.objects.filter(team__in=mentor.teams.all())
            }

            return render(self.request, "user/mentor.html", context)

        # condidate user :
        condidate = Candidate.objects.get(user_ptr_id=user.id)
        context = {
            "team": condidate.team,
            "voices": Voice.objects.filter(owner=condidate)
        }

        return render(self.request, "user/candidate.html", context)
