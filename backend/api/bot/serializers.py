from rest_framework import serializers
from apps.users.models import BotUser


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
        
        
        
        
