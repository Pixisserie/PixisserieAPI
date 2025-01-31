from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('check/username/', views.CheckUsernameView.as_view()),
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]