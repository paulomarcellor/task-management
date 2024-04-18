from rest_framework import serializers
from tasks.models import dataTask, stepsTask

class dataTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataTask
        fields = '__all__'

class stepsTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = stepsTask
        fields = '__all__'
