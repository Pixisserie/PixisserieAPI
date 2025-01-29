from django.urls import path
from .views import score_create_or_update

urlpatterns = [
    path('score/', score_create_or_update, name='teddyrun-score-update'),
]