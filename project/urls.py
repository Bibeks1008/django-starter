"""project URL Configuration"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user.views import UserSignupView

schema_view = get_schema_view(
   openapi.Info(
      title="API DOCUMENTATION",
      default_version='v1',
      description="Stock Price Monitoring",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
      authentication_classes=[]
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('', include('ramailo.urls')),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('user.urls')),
    path('', include('stock_price_tracking.urls')),
]

urlpatterns += staticfiles_urlpatterns()
