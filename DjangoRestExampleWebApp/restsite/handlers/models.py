from django.db import models
from enum import Enum
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

class TaskStatus(Enum):
    Unknown = 'unknown'
    Started = 'started'
    Complete = 'complete'
    Abandon = 'abandon'

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    # Note: 'related_name' must set correctly
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(choices=[(status.value, status.name) for status in TaskStatus], default=TaskStatus.Unknown.value, max_length=100)
    finished_at = models.DateTimeField(null=True, blank=True)
    # content_link = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.title}: id: {self.id}, owner: {self.owner}, status: {self.status}, created_at: {self.created_at}, finished_at: {self.finished_at}, content_link: {self.content_link}' 

    def save(self, *args, **kwargs):
        # we can customize the save operation
        super().save(*args, **kwargs) 

    class Meta:
        ordering = ['created_at']