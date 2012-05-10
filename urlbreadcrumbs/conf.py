# TODO: make this compatible with django-appconf

from django.conf import settings

NAME_MAPPING = getattr(settings, 'URLBREADCRUMBS_NAME_MAPPING', {})

