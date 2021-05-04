from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User 
        fields = [              
            "username",
            "email",
            "password",
        ]
       
        


    	