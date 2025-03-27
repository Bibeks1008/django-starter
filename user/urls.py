from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import UserSignupView

urlpatterns = [
  path("user/register/", UserSignupView.as_view(), name="register"),
  path("token/", TokenObtainPairView.as_view(), name="get_token"),
  path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
]
