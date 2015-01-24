from django.conf.urls import patterns, url
from account import views

urlpatterns = patterns('',
                       # /shayan72
                       url(r'^(?P<username>\w+)$', views.home, name='home'),
)