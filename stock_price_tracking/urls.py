from django.urls import path
from .views import StockView, StockTrackingView

urlpatterns = [
  path('view-stocks/', StockView.as_view()),
  path('stock-tracking/', StockTrackingView.as_view(), name='create-stock-tracking')
]