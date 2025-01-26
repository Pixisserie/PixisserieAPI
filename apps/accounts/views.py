from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
                            SignupSerializer,
                        )
from rest_framework.exceptions import ValidationError
import logging
from django.contrib.auth import get_user_model

logger = logging.getLogger("accounts.views")
User = get_user_model()

@permission_classes([AllowAny])
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        try:
            # 객체 저장 시도
            serializer.save()
            logger.info("Successfully created an object.")
        except Exception as e:
            # 예외 발생 시 로그 기록
            logger.error(f"Error occurred while creating an object: {str(e)}")
            raise ValidationError({"detail": f"An error occurred: {str(e)}"})