from django.db import models
from django.contrib.auth.models import User

class TrainerProfile(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trainerprofile")
    email = models.EmailField()
    is_active = models.BooleanField(default=False)  # account inactive until admin approval
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"
