from django.conf.urls import url

from .views import (
    ListCreateCourse,
 )

urlpatterns = [
    url(r'^$',ListCreateCourse.as_view(),name = 'course_list'),

]