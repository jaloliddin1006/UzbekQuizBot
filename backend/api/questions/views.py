from apps.question.models import Question, UserQuestionAnswer
from api.questions.serializers import QuestionSerializer, UserQuestionAnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class QuestionListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__user_id', 'subject']
    

    
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
    

    