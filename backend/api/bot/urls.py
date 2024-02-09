from django.urls import path
from api.bot.views import BotUserListCreateView, BotUserRetrieveUpdateDestroyView

urlpatterns = [
    path('create-list/', BotUserListCreateView.as_view(), name='bot-user-list-create'),
    path('update-delete/<str:user_id>/', BotUserRetrieveUpdateDestroyView.as_view(), name='bot-user-retrieve-update-destroy'),
]