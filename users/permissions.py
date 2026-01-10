# users/permissions.py
from rest_framework.permissions import BasePermission

class AdminOnly(BasePermission):
    """
    Allows access only to admin users (superusers).
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class TrainerOnly(BasePermission):
    """
    Allows access only to users with a Trainer profile.
    """
    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, "trainerprofile"))


class BeneficiaryOnly(BasePermission):
    """
    Allows access only to users with a Beneficiary profile.
    """
    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, "beneficiaryprofile"))

