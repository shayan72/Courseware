from django.conf.urls import include, patterns, url
from course import views

urlpatterns = patterns('',
                       # /courses/
                       url(r'^$', views.courses, name='courses'),

                       # /courses/93-94/FA/
                       url(
                           r'^(?P<course_year_1>\d{2})-(?P<course_year_2>\d{2})/(?P<term>\w{2})/', include(patterns('',
                                        url( r'^$', views.courses, name='courses_of_term' ),
                                        url( r'^ce(?P<course_num>\d+)-(?P<course_group>\d+)/', include(patterns('',
                                            url( r'^$', views.course_page, name='course_page'),
                                            url( r'^syllabus$', views.course_syllabus, name='course_syllabus' ),
                                            url( r'^calendar$', views.course_calendar, name='course_calendar' ),
                                            url( r'^assignments$', views.course_assignments, name='course_assignments' ),
                                            url( r'^grades$', views.course_grades, name='course_grades' ),
                                            url( r'^videolectures$', views.course_videolectures, name='course_videolectures' ),
                                            url( r'^resources$', views.course_resources, name='course_resources' ),
                                            url( r'^forum$', views.course_forum, name='course_forum' ),
                                                                                                       ))
                                        ),
                                                                                                                ))
                       ),
)