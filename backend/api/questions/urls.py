from django.urls import path
from api.questions.views import (
    QuestionListCreateView, 
    QuestionRetrieveUpdateDestroyView,
    UserQuestionAnswerListCreateView,
)

urlpatterns = [
    path('create-list/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('update-delete/<str:code>/', QuestionRetrieveUpdateDestroyView.as_view(), name='question-update-delete'),
    path('user-question-answer/create-list/', UserQuestionAnswerListCreateView.as_view(), name='user-question-answer-create-list'),
]
