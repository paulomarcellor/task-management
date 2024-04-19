from rest_framework import serializers
from tasks.models import dataTask, stepsTask

class dataTaskSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()
    class Meta:
        model = dataTask
        fields = '__all__'
    
    def get_days(self, obj):
        diferenca = obj.deadline - obj.start
        return diferenca.days

class stepsTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = stepsTask
        fields = '__all__'
