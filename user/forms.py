from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from team.models import Team
from user.models import Candidate

User = get_user_model()


class Authentication(AuthenticationForm):

    help_texts = {
        'username': _("Phone"),
        'password': _("Password"),
    }

    def __init__(self, *args, **kwargs):
        super(Authentication, self).__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs['placeholder'] = self.help_texts[field[0]]


class Registration(UserCreationForm):

    class Meta:
        model = Candidate
        fields = ['phone', 'password1', 'password2', 'team', 'email']
        widgets = {
            "team": forms.Select(choices=[(team.id, team.name) for team in Team.objects.all()], attrs={
                "required": True,
            })
        }
        help_texts = {
            'phone': _("Phone"),
            'email': _("Email (Optional)"),
            'team': _("Please select a team"),
            'password1': _("Password"),
            'password2': _("Confirm Password"),
        }

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs['placeholder'] = self.Meta.help_texts[field[0]]



