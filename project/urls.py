"""project URL Configuration"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import UserSignupView

urlpatterns = [
    # path('', include('ramailo.urls')),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('', include('user.urls')),
    path('', include('stock_price_tracking.urls')),
]

urlpatterns += staticfiles_urlpatterns()
