from rest_framework import serializers
from .models import *

class CarsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Cars
    fields = ('id', 'name', 'number', 'company')