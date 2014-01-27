#!/usr/bin/env python
import os
import sys

from django.conf import settings
from django.conf import global_settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'urlbreadcrumbs',
            'urlbreadcrumbs.tests',
        ),
        SITE_ID=1,
        SECRET_KEY='super-secret',
        ROOT_URLCONF='urlbreadcrumbs.tests.urls',
        TEMPLATE_CONTEXT_PROCESSORS = \
            global_settings.TEMPLATE_CONTEXT_PROCESSORS + \
            (
             'django.core.context_processors.request', # for ``render_breadcrumbs`` templatetag
             'urlbreadcrumbs.context_processors.build_breadcrumbs',
            ),
        URLBREADCRUMBS_NAME_MAPPING = {
            'index'  : 'A title for a home page',
            't1home' : 'Index page of Test1',
        }
    )


from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['urlbreadcrumbs', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])

