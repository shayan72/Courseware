from django.conf.urls import patterns, url
from account import views

urlpatterns = patterns('',
                       # /user/
                       url(r'^$', views.home, name='home'),
                       url(r'^login$', views.my_login, name='my_login'),
                       url(r'^logout$', views.my_logout, name='my_logout'),
)