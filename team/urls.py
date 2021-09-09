from django.urls import path
from .views import TeamList, TeamDetail

from team.models import Team

app_name = "team"
urlpatterns = [
    path('list/', TeamList.as_view(), name='list'),
    path('detail/<int:pk>', TeamDetail.as_view(), name='detail'),
]
