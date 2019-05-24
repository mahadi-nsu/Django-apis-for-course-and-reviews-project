from django.conf.urls import url
from django.urls import path

from .views import (
    ListCreateCourse,
    RetrieveUpdateDestroyCourse,
    ListCreateReview,
    RetrieveUpdateDestroyReview,
 )

urlpatterns = [
    path('',
        ListCreateCourse.as_view() , 
        name = "course-lists"),
    path('<int:pk>/',
        RetrieveUpdateDestroyCourse.as_view(),
        name='course-lists-details'),
    path('<int:pk>/reviews',
        ListCreateReview.as_view(),
        name='course-review')    
        
]