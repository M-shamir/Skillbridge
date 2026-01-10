from django.urls import path
from .views import TrainerRegisterView,ApproveTrainerView,PendingTrainerListView,ApprovedTrainerListView



urlpatterns = [
    path("register/", TrainerRegisterView.as_view(), name="trainer_register"),
    path("pending/", PendingTrainerListView.as_view(),name="trainer-pending-list"),
    path("approve/", ApproveTrainerView.as_view(),name="trainer-approve"),
    path("trainers/approved/", ApprovedTrainerListView.as_view(), name="approved-trainers"),
]
