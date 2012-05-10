from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^aaa/$', direct_to_template, {'template' : 't2sub.html'}, name='t2aaa'),
)
