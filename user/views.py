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
  # queryset = User.objects.all()
  # serializer_class = UserSerializer

  # def post(self, request, *args, **kwargs):
  #   user, errors = UserService.create_user(request.data)
        
  #   if errors:
  #     return ResponseBuilder().bad_request_400().get_response()
        
        
  #   return ResponseBuilder().ok_200().result_object({"message": "Admin Created!", "userId": user.id}).get_response()

  # def get(self, request, *args, **kwargs):
  #   users = User.objects.all()
  #   serializer = self.serializer_class(users, many=True)

  #   return ResponseBuilder().ok_200().result_object(serializer.data).get_response()
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]




