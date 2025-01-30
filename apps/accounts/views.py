from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import (
                            SignupSerializer,
                        )
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
import logging
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

logger = logging.getLogger("accounts.views")
User = get_user_model()

@permission_classes([AllowAny])
class CheckUsernameView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        username = request.query_params.get('username')
        
        if not username:
            return Response({"error": "username을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
        is_exist = User.objects.filter(username=username).exists()

        if is_exist:
            return Response({"available": False, "message": "해당 유저네임이 이미 존재합니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"available": True, "message": "유저네임 설정 가능"}, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        try:
            # 객체 저장 시도
            serializer.is_valid()
            user = serializer.save()
            logger.info("Successfully created an object.")

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                "refresh": refresh_token,
                "access": access_token,
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            # 예외 발생 시 로그 기록
            logger.error(f"Error occurred while creating an object: {str(e)}")
            raise ValidationError({"detail": f"An error occurred: {str(e)}"})