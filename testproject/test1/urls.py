from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from urlbreadcrumbs import url as burl

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template' : 't1.html'}, name='t1home'),
    burl(r'^aaa/$', direct_to_template, {'template' : 't1sub.html'}, name='t1aaa', verbose_name = "Test1 subpage"),
)
