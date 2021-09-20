from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from team.models import Team
from user.forms import Authentication, Registration
from django.utils.translation import gettext_lazy as _


class Login(SuccessMessageMixin, FormView):
    form_class = Authentication
    template_name = "registration/login.html"
    success_url = reverse_lazy("user:login")
    success_message = _("Wellcome") + " %(username)s !"

    def form_valid(self, form):
        login(self.request, user=form.get_user())
        return super().form_valid(form)


class Register(SuccessMessageMixin, FormView):
    form_class = Registration
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user:register')
    success_message = _("Candidates was created successfully!")

    def get_context_data(self, **kwargs):
        kwargs['status'] = None if Team.objects.all() else _("The registration has been disabled!")
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


