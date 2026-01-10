from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrainerRegistrationSerializer
from rest_framework.permissions import AllowAny

class TrainerRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TrainerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            trainer = serializer.save()
            return Response({
                "id": trainer.id,
                "username": trainer.user.username,
                "email": trainer.email,
                "status": trainer.status,
                "message": "Trainer registered successfully. Pending admin approval."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
