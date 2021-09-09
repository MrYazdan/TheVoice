from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from team.models import Team
from user.models import Candidate, Mentor


class Handler(LoginRequiredMixin, View):

    def get(self):
        # check user type:
        user = self.request.user
        # annonymous user -> redirect to login page
        # admin user :
        if user.is_admin:
            context = {
                "teams": [Team.objects.all()],
                "mentors": [Mentor.objects.all()],
                "candidates": [Candidate.objects.all()],
            }

        # mentor user :
        elif user.is_mentor:
            context = {
                "teams": [user.teams.all()],
                "candidates": [Candidate.objects.filter(team=team) for team in user.teams.all()],
            }

        # condidate user :
        context = {
            "team": Candidate.objects.get(user=user).team,
        }

        return render(self.request, "", context)