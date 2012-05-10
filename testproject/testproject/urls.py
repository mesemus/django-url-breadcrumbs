from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from urlbreadcrumbs import url as burl

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template' : 'index.html'}, name='index'),
    burl(r'^test1/', include('test1.urls')),
    url(r'^test2/', include('test2.urls')),
)
