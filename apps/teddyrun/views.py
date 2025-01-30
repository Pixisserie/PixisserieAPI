from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Score
from .serializers import RunScoreSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
import logging
logger = logging.getLogger("teddyrun.views")

def score_get_or_create(user):
    is_exsist = Score.objects.filter(user=user).exists()
    if not is_exsist:
        run_score = Score.objects.create(user=user, score=0)
    else:
        run_score = Score.objects.get(user=user)
    return run_score

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def score_create_or_update(request):
    user = request.user
    run_score = score_get_or_create(user)
    serializer = RunScoreSerializer(data=request.data, instance=run_score)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def score_ranking(request):
    scores = Score.objects.all().order_by('-score')
    serializer = RunScoreSerializer(scores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)