from rest_framework import viewsets
from .models import CleaningService, Booking
from .serializers import CleaningServiceSerializer, BookingSerializer

class CleaningServiceViewSet(viewsets.ModelViewSet):
    queryset = CleaningService.objects.all()
    serializer_class = CleaningServiceSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
