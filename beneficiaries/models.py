from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class BeneficiaryProfile(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="beneficiaryprofile")
    age = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    documents = models.TextField(blank=True, null=True)  # Can be file paths or URLs
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"
