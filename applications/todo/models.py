from django.db import models
from enum import Enum

# Create your models here.
class List(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, max_length=1000)

    def __str__(self):
        return self.name


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(models.Model):

    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, max_length=1000)
    due_datetime = models.DateTimeField()
    status = models.CharField(
        max_length=5, choices=[(choice, choice.value) for choice in TaskStatus]
    )
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
