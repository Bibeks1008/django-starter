from django.urls import path
from .views import StockView, StockTrackingView

urlpatterns = [
  path('home/', StockView.as_view()),
  path('create-stock-tracking/', StockTrackingView.as_view(), name='create-stock-tracking')
]