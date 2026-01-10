# beneficiaries/urls.py
from django.urls import path
from .views import BeneficiaryRegisterView, PendingBeneficiariesListView, ApproveBeneficiaryView


urlpatterns = [
    
    path("register/", BeneficiaryRegisterView.as_view(), name="beneficiary_register"),
    path("pending/", PendingBeneficiariesListView.as_view(), name="pending_beneficiaries"),
    path("approve/", ApproveBeneficiaryView.as_view(), name="approve_beneficiary"),
]
