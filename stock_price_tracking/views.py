from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.mail import send_mail

from .accessor import StockAccessor
from ramailo.builders.response_builder import ResponseBuilder
from .stock_price_service import StockTrackingService
from .serializers import StockTrackingSerializer

# Create your views here.
class StockView(APIView):

  def get(self, request):
    stock_list = StockAccessor().get_stock_price()
    return ResponseBuilder().ok_200().result_object(stock_list).get_response()

class StockTrackingView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
      stock_details = StockTrackingService.get_stock_tracked(request.user)
      serialized_data = StockTrackingSerializer(stock_details,many=True).data
      return ResponseBuilder().ok_200().result_object(serialized_data).get_response()

  def post(self, request):
      stock_tracking, errors = StockTrackingService.create_stock_tracking(request.data, request.user)

      if stock_tracking:
        serialized_data = StockTrackingSerializer(stock_tracking).data 
        return ResponseBuilder().ok_200().result_object(serialized_data).get_response()
      else:
        return Response({
            "message": "Invalid data",
            "errors": errors or {}
        }, status=status.HTTP_400_BAD_REQUEST)