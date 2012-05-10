from django.core.urlresolvers import RegexURLPattern, get_resolver, Resolver404, RegexURLResolver, resolve
from django.conf import settings
from urlbreadcrumbs.url_hacks import BreadRegexURLResolver

from urlbreadcrumbs.conf import NAME_MAPPING

def build_breadcrumbs(request):

    resolver = BreadRegexURLResolver(r'^/', settings.ROOT_URLCONF)
    ret_list = [] # list of pairs (name, path)

    path = request.path_info
    parts = path.split("/")
    if not parts[-1]: parts = parts[:-1] # loose last empty element
    try_path = ""
    for part in parts:
        try_path = try_path + part + "/"

        try:

            resolver_match = resolver.resolve(try_path)
            if resolver_match is not None:

                nspace, url_name = resolver_match.namespace, resolver_match.url_name
                lookup = url_name
                if nspace:
                    lookup = nspace + ":" + url_name

                from_mapping = NAME_MAPPING.get(lookup, False)
                if from_mapping:
                    name = from_mapping
                elif hasattr(resolver_match, 'breadcrumb_verbose_name') and resolver_match.breadcrumb_verbose_name is not None:
                    name = resolver_match.breadcrumb_verbose_name
                else:
                    name = resolver_match.url_name

                ret_list.append((name, try_path))

        except Resolver404:
            pass

    return { 'breadcrumbs' : ret_list }

