from django.urls import path, include

from api import bot_urls, questions_urls

urlpatterns = [
    path('users/', include(bot_urls)),
    path('questions/', include(questions_urls)),
    
]