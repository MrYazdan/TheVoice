from django.urls import path
from .views import ScoreList, ScoreDetail

app_name = "score"
urlpatterns = [
    path('list/', ScoreList.as_view(), name='list'),
    path('detail/<int:pk>', ScoreDetail.as_view(), name='detail'),
]
