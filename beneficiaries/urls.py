# beneficiaries/urls.py
from django.urls import path
from .views import BeneficiaryRegisterView


urlpatterns = [
    
    path("register/", BeneficiaryRegisterView.as_view(), name="beneficiary_register"),

    # Future endpoints (admin approve, list, etc.) can be added here
    # path("approve/<int:pk>/", BeneficiaryApproveView.as_view(), name="beneficiary_approve"),
    # path("", BeneficiaryListView.as_view(), name="beneficiary_list"),
]
