from apps.question.models import Question, UserQuestionAnswer
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_id', read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
        # extra_kwargs = {
        #     'user': {'read_only': True},
        # }
        
class UserQuestionAnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_id')
    question = serializers.CharField(source='question.code')
    class Meta:
        model = UserQuestionAnswer
        fields = '__all__'
       