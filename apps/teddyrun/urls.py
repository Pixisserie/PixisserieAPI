from django.urls import path
from . import views

urlpatterns = [
    path('score/', views.score_create_or_update, name='teddyrun-score-update'),
    path('rank/', views.score_ranking, name='teddyrun-rank'),
]