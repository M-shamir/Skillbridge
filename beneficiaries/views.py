from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BeneficiaryRegistrationSerializer, BeneficiaryApproveSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from .services import approve_beneficiary
from .models import BeneficiaryProfile
from rest_framework.permissions import AllowAny

class BeneficiaryRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = BeneficiaryRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            beneficiary = serializer.save()
            return Response({
                "id": beneficiary.id,
                "username": beneficiary.user.username,
                "email": beneficiary.user.email,
                "status": beneficiary.status,
                "message": "Beneficiary registered successfully. Pending admin approval."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PendingBeneficiariesListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        pending = BeneficiaryProfile.objects.filter(status="PENDING", is_deleted=False)
        data = [
            {
                "id": b.id,
                "username": b.user.username,
                "email": b.user.email,
                "age": b.age,
                "category": b.category.name if b.category else None,
                "created_at": b.created_at,
            }
            for b in pending
        ]
        return Response(data)

class ApproveBeneficiaryView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = BeneficiaryApproveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        beneficiary_id = serializer.validated_data["id"]
        beneficiary, password_or_msg = approve_beneficiary(beneficiary_id)

        if not beneficiary:
            return Response({"error": password_or_msg}, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "id": beneficiary.id,
            "username": beneficiary.user.username,
            "email": beneficiary.user.email,
            "status": beneficiary.status,
            "password_sent": True  
        })
