from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    stock_symbol = models.CharField(max_length=10, unique=True)
   

    def __str__(self):
        return self.name


class StockTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracked_stocks')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='trackers')
    price_increase_trigger = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_decrease_trigger = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # You can add fields for the last notified date to avoid sending notifications multiple times
    last_notified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} tracks {self.company.name}"

    class Meta:
        unique_together = ('user', 'company')  # A user can only track a company once.