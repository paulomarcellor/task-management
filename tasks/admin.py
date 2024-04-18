from django.contrib import admin
from tasks.models import dataTask, stepsTask

admin.site.register(dataTask)
admin.site.register(stepsTask)