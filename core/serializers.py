from rest_framework import serializers
from .models import CleaningService, Booking

class CleaningServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningService
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
