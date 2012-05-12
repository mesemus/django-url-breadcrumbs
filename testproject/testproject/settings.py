# Django settings for testproject project.
import os
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates')
)

from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + \
    ('urlbreadcrumbs.context_processors.build_breadcrumbs',)

INSTALLED_APPS = (
    'urlbreadcrumbs',
    'test1',
    'test2',
)

URLBREADCRUMBS_NAME_MAPPING = {
    'index'  : 'Home page',
    't1home' : 'Index page of Test1',
}

URLBREADCRUMBS_RESOLVER = 'urlbreadcrumbs.BreadRegexURLResolver'

