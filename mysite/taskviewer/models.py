from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

