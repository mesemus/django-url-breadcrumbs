from django.conf.urls import patterns, include, url
# from django.views.generic.simple import direct_to_template
from urlbreadcrumbs.tests.views import simple_view, simple_view_with_arg

from urlbreadcrumbs import url as burl

test1_urls = patterns('',
                      url(r'^$', simple_view,
                          {'template' : 'urlbreadcrumbs_tests/t1.html'},
                          name='t1home'),
                      burl(r'^aaa/$', simple_view,
                           {'template' : 'urlbreadcrumbs_tests/t1sub.html'},
                           name='t1aaa',
                           verbose_name = 'Test1 subpage via custom url function'),
                      url(r'^aaa/(?P<pk>\d+)/$', simple_view_with_arg,
                          {'template' : 'urlbreadcrumbs_tests/t1sub.html'},
                          name='t1aaa_pk'),
                      url(r'^bbb/(?P<pk>\d+)/$', simple_view_with_arg,
                          {'template' : 'urlbreadcrumbs_tests/t1sub.html'},
                          name='t1bbb_pk'),
                      burl(r'^ccc/(?P<pk>\d+)/$', simple_view_with_arg,
                           {'template' : 'urlbreadcrumbs_tests/t1sub.html'},
                           name='t1ccc_pk',
                           verbose_name='Test1 subpage via custom url with context var {{ pk }}'),
                      )

test2_urls = patterns('',
                      burl(r'^aaa/$', simple_view,
                           {'template' : 'urlbreadcrumbs_tests/t2sub.html'},
                           name='t2aaa',
                           verbose_name='T2 test page'),
                      )


urlpatterns = patterns('',
                       url(r'^$', simple_view,
                           {'template' : 'urlbreadcrumbs_tests/index.html'},
                           name='index'),
                       burl(r'^test1/', include(test1_urls)),
                       url(r'^test2/', include(test2_urls)),
                       url(r'^test1_namespace/', include(test1_urls, namespace='test1ns')),
                       )
