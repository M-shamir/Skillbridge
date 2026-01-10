from django.urls import path
from .views import TrainingSessionListCreateAPIView

urlpatterns = [
    path("", TrainingSessionListCreateAPIView.as_view(), name="training-session-list-create"),
]
