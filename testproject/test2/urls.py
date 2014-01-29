from django.conf.urls import patterns, include, url
from urlbreadcrumbs import url
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
    url(r'^aaa/$', TemplateView.as_view(template_name = 't2sub.html'), name='t2aaa', verbose_name="T2 test page"),
)
