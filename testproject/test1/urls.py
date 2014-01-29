from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from urlbreadcrumbs import url as burl

urlpatterns = patterns('',
    url(r'^$',      TemplateView.as_view(template_name = 't1.html'),    name='t1home'),
    burl(r'^aaa/$', TemplateView.as_view(template_name = 't1sub.html'), name='t1aaa', verbose_name = "Test1 subpage via custom url function"),
)
