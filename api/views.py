from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Message
from .serializers import UserSerializer, MessageSerializer, ConversationListSerializer

class UserView(APIView):
    permission_classes = [AllowAny]

    # get user information
    def get(self, request, format=None):
        user = User.objects.get(id=request.GET['id'])
        serializer = UserSerializer(user)

        return Response(serializer.data)

    # create user
    def post(self, request, format=None):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    # get all list of people the user had conversations with
    def get(self, request, format=None):
        sender = request.user

        if 'recipient' in request.GET:
            messages = Message.objects.filter(sender=sender, recipient=request.GET['recipient'])
            serializer = Message(messages, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            conversations = Message.objects.filter(sender=sender).values('recipient').distinct()

            serializer = ConversationListSerializer(conversations, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        post_details = request.POST
        sender = request.user
        recipient = User.objects.get(id=post_details['recipient'])
        content = post_details['content']
        pub_date = datetime.now()

        message = Message(
            sender=sender,
            recipient=recipient,
            content=content,
            pub_date=pub_date
        )
        message.save()

        serializer = MessageSerializer(message)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)