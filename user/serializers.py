from rest_framework import serializers
from django.contrib.auth.models import User

from shared.helpers.logging_helper import logger

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True 

    def create(self, validated_data):
        logger.info(validated_data)
        user = User.objects.create_user(**validated_data)
        return user