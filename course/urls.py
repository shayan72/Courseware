from django.conf.urls import patterns, url
from course import views

urlpatterns = patterns(  '',
                       url( r'^$', views.courses, name='courses' ),
                       )