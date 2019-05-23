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


class ListCreateCourse(APIView):
    def get(self,request,format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CourseSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
