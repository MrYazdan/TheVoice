from django.urls import path
from .views import TeamList, TeamDetail

app_name = "team"
urlpatterns = [
    path('list/', TeamList.as_view(), name='list'),
    path('detail/<int:pk>', TeamDetail.as_view(), name='detail'),
]
