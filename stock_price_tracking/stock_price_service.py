from .models import StockTracking
from .serializers import StockTrackingSerializer

from shared.helpers.logging_helper import logger

class StockTrackingService:
    @staticmethod
    def create_stock_tracking(data, user):
      try:
        serializer = StockTrackingSerializer(data=data, context={'user': user})
        if serializer.is_valid():
            stock_tracking = serializer.save()
            return stock_tracking, {}
        else:
            return {}, serializer.errors
      except Exception as e:
        logger.error(f"Unexpected error during stock tracking creation: {e}")
        return {}, {"non_field_errors": ["An unexpected error occurred."]}

    @staticmethod
    def get_stock_tracked(user):
      stock_details = StockTracking.objects.filter(user=user).select_related('company','user').all()
      return stock_details

