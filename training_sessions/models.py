from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class TrainingSession(models.Model):
    topic = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sessions")
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trainer_sessions")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meeting_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.topic} - {self.category.name}"
