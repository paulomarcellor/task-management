from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import dataTask, stepsTask
from tasks.serializers import dataTaskSerializer, stepsTaskSerializer

import requests

def index(request):
    api_url = "http://127.0.0.1:8000/api/datatasks/"
    response = requests.get(api_url)
    tasks = response.json() if response.status_code == 200 else []
    return render(request, 'index.html', {'tasks': tasks})

def registration(request):
    fields = ["ID", "Task", "Status", "Steps", ""]
    return render(request, 'registration.html', {'fields': fields})

# API

class dataTaskViewset(viewsets.ModelViewSet):
    queryset = dataTask.objects.all()
    serializer_class = dataTaskSerializer

class stepsTaskViewset(viewsets.ModelViewSet):
    queryset = stepsTask.objects.all()
    serializer_class = stepsTaskSerializer