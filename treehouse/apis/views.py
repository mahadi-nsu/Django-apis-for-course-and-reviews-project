from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Course,
    Review,
)

from .serializers import (
    CourseSerializer,
    ReviewSeriaizer,
    
)    

class ListCreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer