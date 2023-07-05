from django.contrib.auth.models import User, Group
from django.db import models
from enum import Enum

class TaskStatus(Enum):
    Unknown = 'unknown'
    Started = 'started'
    Complete = 'complete'
    Abandon = 'abandon'

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    # owner = models.ForeignKey(auth.User, on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=[(status.value, status.name) for status in TaskStatus], default=TaskStatus.Unknown.value, max_length=100)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}: id: {self.id}, status: {self.status}, created_at: {self.created_at}, finished_at: {self.finished_at}'  

    class Meta:
        ordering = ['created_at']