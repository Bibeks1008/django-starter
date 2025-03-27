import logging
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone

from stock_price_tracking.models import StockTracking
from stock_price_tracking.accessor import StockAccessor

# Set up logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fetch stock prices every 15 minutes and notify users if triggers are met'
    print("Starting the fetch_stock_prices command...")

    def handle(self, *args, **kwargs):
        stock_accessor = StockAccessor()
        stock_data = stock_accessor.get_stock_price()

      
        stock_trackings = StockTracking.objects.all()

        for tracking in stock_trackings:
            company_symbol = tracking.company.stock_symbol
            if company_symbol in stock_data:
                stock_price = stock_data[company_symbol]

                
                if stock_price:
                    
                    if tracking.price_increase_trigger and stock_price >= float(tracking.price_increase_trigger):
                        self.send_alert(tracking, stock_price, 'increase')

                    
                    if tracking.price_decrease_trigger and stock_price <= tracking.price_decrease_trigger:
                        self.send_alert(tracking, stock_price, 'decrease')

        print("Finished the fetch_stock_prices command.")

    def send_alert(self, tracking, stock_price, trigger_type):
        
        user = tracking.user
        company_name = tracking.company.name
        company_symbol = tracking.company.stock_symbol

        
        if trigger_type == 'increase':
            message = f"Hello {user.username},\n\nThe stock price of {company_name} ({company_symbol}) has increased to {stock_price}. Your trigger price was {tracking.price_increase_trigger}."
        else:
            message = f"Hello {user.username},\n\nThe stock price of {company_name} ({company_symbol}) has decreased to {stock_price}. Your trigger price was {tracking.price_decrease_trigger}."

        
        try:
            send_mail(
                subject=f"{company_name} Stock Price Alert",
                message=message,
                from_email="dreamhigh.bibek@gmail.com",  
                recipient_list=[user.email],
                fail_silently=False,
            )
            logger.info(f"Sent email to {user.email} for {company_name} ({company_symbol})")
            
            tracking.last_notified = timezone.now()
            tracking.save()
        except Exception as e:
            logger.error(f"Error sending email to {user.email}: {e}")

