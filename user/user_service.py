from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer

class UserService:
    @staticmethod
    def create_user(user_data):
        serializer = UserSerializer(data=user_data)
        if not serializer.is_valid():
            return None, serializer.errors

        
        password = serializer.validated_data['password']
        serializer.validated_data['password'] = make_password(password)

      
        user = serializer.save()
        return user, None  