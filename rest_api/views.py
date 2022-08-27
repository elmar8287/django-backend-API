from rest_framework import viewsets
from .serializers import CarsSerializer
from .models import Cars

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all().order_by('name')
    serializer_class = CarsSerializer
