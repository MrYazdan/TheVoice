from django.urls import path
from .views import Handler

app_name = 'settings'
urlpatterns = [
    path("", Handler.as_view(), name="index"),
]
