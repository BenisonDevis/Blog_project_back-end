from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class BlogCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'