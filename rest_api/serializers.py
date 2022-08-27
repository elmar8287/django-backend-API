from rest_framework import serializers
from .models import *

class CarsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Cars
    fields = ('id', 'name', 'number', 'company')

class DaysSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Days
    fields = ('id', 'name','note')

class BookingSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Booking
    fields = ('id', 'name','day','car')