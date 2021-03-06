from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Courseware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^courses/', include('course.urls')),
    url(r'^manage/', include('course_admin.urls')),
    url(r'^user/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
