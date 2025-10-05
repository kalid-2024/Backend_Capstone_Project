from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.title} - {'Completed' if self.completed else 'Pending'}"