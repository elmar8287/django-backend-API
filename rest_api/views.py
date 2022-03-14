from rest_framework import viewsets
from .serializers import CoursesSerializer
from .models import Courses

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by('name')
    serializer_class = CoursesSerializer
