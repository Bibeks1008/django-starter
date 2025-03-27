from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from ramailo.builders.response_builder import ResponseBuilder
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .user_service import UserService

class UserSignupView(generics.CreateAPIView):

  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]




