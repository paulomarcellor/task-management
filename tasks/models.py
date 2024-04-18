from django.db import models
#from django.core.validators import MaxValueValidator

class dataTask(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    start = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=100)
    aap = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class stepsTask(models.Model):
    task = models.ForeignKey(dataTask, on_delete=models.CASCADE)
    step = models.CharField(max_length=200)
    step_start = models.DateField()
    step_end = models.DateField()
    done = models.BooleanField(default=False)
