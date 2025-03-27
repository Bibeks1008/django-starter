from .models import StockTracking
from .serializers import StockTrackingSerializer


class StockTrackingService:
    @staticmethod
    def create_stock_tracking(data, user):
      try:
        serializer = StockTrackingSerializer(data=data, context={'user': user})
        if serializer.is_valid():
            stock_tracking = serializer.save()
            return stock_tracking, None
        else:
            return None, serializer.errors
      except Exception as e:
        print(f"Unexpected error during stock tracking creation: {e}")
        return None, {"non_field_errors": ["An unexpected error occurred."]}

    @staticmethod
    def get_stock_tracked(user):
      stock_details = StockTracking.objects.filter(user=user).select_related('company','user').all()
      return stock_details

