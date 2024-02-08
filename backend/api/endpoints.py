from django.urls import path, include

from api.bot import urls

urlpatterns = [
    path('users/', include(urls)),
]