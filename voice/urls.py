from django.urls import path
from .views import VoiceList, VoiceDetail

app_name = "voice"
urlpatterns = [
    path('list/', VoiceList.as_view(), name='list'),
    path('detail/<int:pk>', VoiceDetail.as_view(), name='detail'),
]
