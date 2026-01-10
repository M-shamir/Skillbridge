from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import TrainingSession
from .serializers import TrainingSessionSerializer
from users.permissions import AdminOnly
from .services import notify_training_session

class TrainingSessionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, AdminOnly]

    def get(self, request):
        sessions = TrainingSession.objects.all()
        serializer = TrainingSessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainingSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session = serializer.save()
        
        notify_training_session(session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

