from django.conf.urls import include, patterns, url
from course_admin import views

urlpatterns = patterns('',

                       # /courses/93-94/1/ce108-1/
                       url(
                           r'^(?P<course_year_1>\d{2})-(?P<course_year_2>\d{2})/(?P<term>\w{2})/ce(?P<course_num>\d+)-(?P<course_group>\d+)/',
                           include(patterns('',
                                            url(r'^$', views.manage_course_page, name='manage_course_page'),
                                            url(r'^syllabus$', views.manage_course_syllabus,
                                                name='manage_course_syllabus'),
                                            url(r'^calendar$', views.manage_course_calendar,
                                                name='manage_course_calendar'),
                                            url(r'^assignments$', views.manage_course_assignments,
                                                name='manage_course_assignments'),
                                            url(r'^grades$', views.manage_course_grades, name='manage_course_grades'),
                                            url(r'^videolectures$', views.manage_course_videolectures,
                                                name='manage_course_videolectures'),
                                            url(r'^resources$', views.manage_course_resources,
                                                name='manage_course_resources'),
                                            url(r'^forum$', views.manage_course_forum, name='manage_course_forum'),

                                            url( r'ajax_add_grades', views.add_course_grades, name = 'ajax_add_grades' ),

                                            url( r'forum/topic/lock', views.ajax_forum_topic_lock, name = 'ajax_forum_topic_lock' ),
                                            url( r'forum/topic/unlock', views.ajax_forum_topic_unlock, name = 'ajax_forum_topic_unlock' ),
                                            url( r'forum/topic/remove', views.ajax_forum_topic_remove, name = 'ajax_forum_topic_remove' ),
                                            url( r'forum/topic/remove', views.ajax_forum_topic_remove, name = 'ajax_forum_topic_remove' ),
                                            url( r'forum/post/remove', views.ajax_forum_post_remove, name = 'ajax_forum_post_remove' ),

                                            url( r'calendar/remove', views.ajax_calendar_remove_item, name = 'ajax_calendar_remove_item' ),
                           ))
                       ),
)