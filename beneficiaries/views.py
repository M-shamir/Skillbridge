from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BeneficiaryRegistrationSerializer
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
