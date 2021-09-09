from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin path :
    path('admin/', admin.site.urls),

    # settings path :
    path('', include("settings.urls")),

    # user path :
    path('', include("user.urls")),
]
