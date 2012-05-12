from django.conf.urls import patterns, include, url
from urlbreadcrumbs import url

urlpatterns = patterns('',
    url(r'^aaa/$', 'django.views.generic.simple.direct_to_template', {'template' : 't2sub.html'}, name='t2aaa', verbose_name="T2 test page"),
)
