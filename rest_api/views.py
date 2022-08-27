from rest_framework import viewsets
from .serializers import *
from .models import *

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all().order_by('name')
    serializer_class = CarsSerializer

class DaysViewSet(viewsets.ModelViewSet):
    queryset = Days.objects.all().order_by('name')
    serializer_class = DaysSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('name')
    serializer_class = BookingSerializer