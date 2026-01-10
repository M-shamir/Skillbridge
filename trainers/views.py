from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrainerRegistrationSerializer, TrainerPendingSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from .models import TrainerProfile
from .services import approve_trainer

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


class PendingTrainerListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        trainers = TrainerProfile.objects.filter(
            status="PENDING",
            is_deleted=False
        )
        serializer = TrainerPendingSerializer(trainers, many=True)
        return Response(serializer.data)
    

class ApproveTrainerView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        trainer_id = request.data.get("id")

        if not trainer_id:
            return Response(
                {"error": "Trainer ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        trainer, msg = approve_trainer(trainer_id)

        if not trainer:
            return Response(
                {"error": msg},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "id": trainer.id,
            "username": trainer.user.username,
            "email": trainer.user.email,
            "status": trainer.status,
            "password_sent": True
        })