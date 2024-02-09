from apps.question.models import Question, UserQuestionAnswer
from rest_framework import serializers
from apps.users.models import BotUser
from django.shortcuts import get_object_or_404

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
        
class UserQuestionAnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_id')
    question = serializers.CharField(source='question.code')
    class Meta:
        model = UserQuestionAnswer
        fields = '__all__'
       