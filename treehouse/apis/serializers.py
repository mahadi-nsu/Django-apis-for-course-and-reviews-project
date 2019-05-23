from rest_framework import serializers

from .models import (
    Course,
    Review,
)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'url',
        )
        model = Course

class ReviewSeriaizer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email' : {'write_only' : True}
        }
        fields =(
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating', 
            'created_at',
        )
        model = Review

