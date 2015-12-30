from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_scans.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'django_scans.views.home', name='home'),
    url(r'^scan$', 'django_scans.views.scan', name='scan'),
    url(r'^scan_csrf_exempt$', 'django_scans.views.scan_csrf_exempt', name='scan_csrf_exempt'),
)
