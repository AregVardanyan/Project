from django.db import models
from .choices import STATUS_CHOICE


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)

    def __str__(self):
        return f"{self.name} {self.created_at}"