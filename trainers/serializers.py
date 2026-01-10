from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TrainerProfile

class TrainerRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = TrainerProfile
        fields = ["username", "email"]

    def create(self, validated_data):
        username = validated_data.pop("username")
        email = validated_data.pop("email")

        # Create inactive user
        user = User.objects.create_user(username=username, email=email, password=None, is_active=False)

        # Create trainer profile
        trainer = TrainerProfile.objects.create(
            user=user,
            email=email,
            status="PENDING",
            is_active=False
        )
        return trainer


class TrainerPendingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = TrainerProfile
        fields = ["id", "username", "email", "created_at"]