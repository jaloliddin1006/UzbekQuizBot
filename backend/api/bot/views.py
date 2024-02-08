from apps.users.models import BotUser
from apps.question.models import Question, UserQuestionAnswer
from api.bot.serializers import BotUserSerializer

## classes with generics 
from rest_framework import generics

class BotUserListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    
    

class BotUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = 'user_id'
    
    