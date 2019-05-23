from django.conf.urls import url

from .views import (
    ListCreateCourse,
    RetrieveUpdateDestroyCourse
 )

urlpatterns = [
    url(r'^$',ListCreateCourse.as_view(),name = 'course_list'),
    url(r'(?P<pk>\d+)/$',
        RetrieveUpdateDestroyCourse.as_view(),
        name = 'course_detail'),

]