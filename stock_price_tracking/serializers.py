from rest_framework import serializers
from .models import Company, StockTracking

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'stock_symbol']

class StockTrackingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()  # Nested serializer for company

    class Meta:
        model = StockTracking
        fields = ['user','company', 'price_increase_trigger', 'price_decrease_trigger']
        read_only_fields = ['user']

    def create(self, validated_data):
        company_data = validated_data.pop('company')  # Extract company data
        user = self.context['user']
        company, created = Company.objects.get_or_create(**company_data)  # Get or create company

        # Create the stock tracking entry
        stock_tracking = StockTracking.objects.create(company=company, user=user, **validated_data)
        return stock_tracking