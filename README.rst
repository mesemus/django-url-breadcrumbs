========================
django-url-breadcrumbs
========================

An app for generic breadcrumbs in Django. More info soon (I hope).

The idea is to make breadcrumbs out of parts of an url path. This application assumes that your url patterns are in a REST style.

i.e. ::

    /                                               # root path
    /application/                                   # root of an app/module
    /application/object_type/                       # list of specific objects
    /application/object_type/some_object/           # details of specific object
    /application/object_type/some_object/edit/      # edit (or any other operations) of a specific object

See ``testproject`` for sample usage.

For now this is developed only against Django 1.4 (I don't know whether is it working or not with the older versions)
