from rest_framework.response import Response
from apps.question.models import Question, UserQuestionAnswer
from api.questions.serializers import QuestionSerializer, UserQuestionAnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from apps.users.models import BotUser

class QuestionCreateView(generics.CreateAPIView):
    permission_classes = []
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    
    def create(self, request, *args, **kwargs):
        print(request.data)
        user = get_object_or_404(BotUser, user_id=request.data['user'])
        request.data['user'] = user.id
        return super().create(request, *args, **kwargs)
    
    """
{
"user": "21212",
"code": "1234dert",
        "subject": "matem",
        "description": "prosta",
        "answers": "{'1':'a','2':'a','3':'a','4':'d'}",
        "file": null,
        "size": 4,
 "start_time": "2024-02-09T02:01:43Z"
}
    """
    
    
class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'code'
    
    
    
    
class UserQuestionAnswerListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = UserQuestionAnswer.objects.all()
    serializer_class = UserQuestionAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__user_id', 'question__code', 'score']
    

    