from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from team.models import Team
from user.models import Candidate, Mentor
from voice.models import Voice


class Handler(LoginRequiredMixin, View):

    def get(self):
        # check user type:
        user = self.request.user
        # annonymous user -> redirect to login page
        # admin user :
        if user.is_superuser:
            context = {
                "teams": [Team.objects.all()],
                "mentors": [Mentor.objects.all()],
                "candidates": [Candidate.objects.all()],
            }

            return render(self.request, "user/admin.html", context)

        # mentor user :
        elif user.is_mentor:
            context = {
                "teams": [user.teams.all()],
                "candidates": [Candidate.objects.filter(team=team) for team in user.teams.all()],
            }

            return render(self.request, "user/mentor.html", context)

        # condidate user :
        context = {
            "team": Candidate.objects.get(user=user).team,
            "voices": Voice.objects.filter(owner=user)
        }

        return render(self.request, "user/candidate.html", context)
