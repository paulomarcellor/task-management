from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import dataTask, stepsTask
from tasks.serializers import dataTaskSerializer, stepsTaskSerializer
import requests
from tasks.forms import taskForm, stepsTaskForm


def index(request):
    api_url = "http://127.0.0.1:8000/api/datatasks/"
    response = requests.get(api_url)
    tasks = response.json() if response.status_code == 200 else []
    return render(request, 'index.html', {'tasks': tasks})

def registration(request):
    api_url = "http://127.0.0.1:8000/api/datatasks/"
    response = requests.get(api_url)
    tasks = response.json() if response.status_code == 200 else []
    fields = ["ID", "Task", "Status", "Steps", ""]
    stepForm = stepsTaskForm
    mainForm = taskForm
    return render(request, 'registration.html', {'fields': fields, 'tasks': tasks, 'stepform':stepForm, 'taskform':mainForm})

# API

class dataTaskViewset(viewsets.ModelViewSet):
    queryset = dataTask.objects.all()
    serializer_class = dataTaskSerializer

class stepsTaskViewset(viewsets.ModelViewSet):
    queryset = stepsTask.objects.all()
    serializer_class = stepsTaskSerializer