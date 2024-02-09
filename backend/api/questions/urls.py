from django.urls import path
from api.questions.views import (
    QuestionCreateView, 
    QuestionRetrieveUpdateDestroyView,
    UserQuestionAnswerListCreateView,
)

urlpatterns = [
    path('create/', QuestionCreateView.as_view(), name='question-create'),
    path('update-delete/<str:code>/', QuestionRetrieveUpdateDestroyView.as_view(), name='question-update-delete'),
    path('user-question-answer/create-list/', UserQuestionAnswerListCreateView.as_view(), name='user-question-answer-create-list'),
]
