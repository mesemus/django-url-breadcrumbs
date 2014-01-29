from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from urlbreadcrumbs import url as burl

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name='index'),
    burl(r'^test1/', include('test1.urls')),
    burl(r'^test2/', include('test2.urls')),
)
