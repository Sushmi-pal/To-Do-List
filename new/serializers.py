from new.models import Todo
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','message']
