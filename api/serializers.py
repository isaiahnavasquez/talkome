from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'last_login']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', 'sender', 'recipient', 'pub_date']

class ConversationListSerializer(serializers.Serializer):
    recipient = serializers.CharField()