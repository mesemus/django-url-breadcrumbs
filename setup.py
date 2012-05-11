import codecs
import re
from os import path
from setuptools import setup


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return open(file_path).read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-url-breadcrumbs',
    version=find_version('urlbreadcrumbs', '__init__.py'),
    description='a generic app to provide a simple breadcrumbs functionality in django projects',
    long_description=read('README.rst'),
    author='Slawek Ehlert',
    author_email='slafs@op.pl',
    license='BSD',
    url='https://bitbucket.org/slafs/django-url-breadcrumbs/',
    packages=[
        'urlbreadcrumbs',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
)
