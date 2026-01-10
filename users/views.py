from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        # 🔹 Detect role
        if user.is_superuser:
            role = "ADMIN"
        elif hasattr(user, "trainerprofile"):
            role = "TRAINER"
        elif hasattr(user, "beneficiaryprofile"):
            role = "BENEFICIARY"
        else:
            return Response(
                {"detail": "User role not assigned"},
                status=status.HTTP_403_FORBIDDEN,
            )

        # 🔹 Create tokens
        refresh = RefreshToken.for_user(user)

        response = Response(
            {
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": role,
                },
            },
            status=status.HTTP_200_OK,
        )

        # 🔹 Store refresh token in HttpOnly cookie
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=True,       # True in production (HTTPS)
            samesite="Strict",
            max_age=7 * 24 * 60 * 60,
        )

        return response
    


class RefreshTokenView(APIView):
    """
    Reads refresh token from cookie and returns a new access token.
    """
    def post(self, request):
        # Read token from cookie
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Refresh token not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Validate and create new access token
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            return Response({"access": access_token})

        except TokenError as e:
            return Response(
                {"error": "Invalid or expired refresh token"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # 🔹 Get refresh token from cookie
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "No refresh token found in cookies"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 🔹 Blacklist the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()  # requires SimpleJWT Blacklist app installed

        except TokenError:
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔹 Clear the cookie
        response = Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie("refresh_token")

        return response