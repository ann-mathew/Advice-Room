from rest_framework import serializers
from .models import Advisor
from django.db import models

class AddAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor 
        fields = [             
            "name",
            "photo_url",
        ]

