# encoding: utf-8

from django.test import TestCase, Client


class BreadcrumbsTest(TestCase):

    def setUp(self):
        if not hasattr(self, 'client'):
            self.client = Client()

    def test_index(self):
        res = self.client.get('/')
        assert res.status_code == 200

        text = 'A title for a home page'
        self.assertContains(res, text, count = 3, html=False)

    def test_sub1(self):
        res = self.client.get('/test1/')
        assert res.status_code == 200

        text = 'Index page of Test1'
        self.assertContains(res, text, count = 3, html=False)

    def test_sub1_with_ns(self):
        res = self.client.get('/test1_namespace/')
        assert res.status_code == 200

        text = 'Index page for namespace version of Test1'
        self.assertContains(res, text, count = 3, html=False)

    def test_sub1_with_ns_and_pk(self):
        res = self.client.get('/test1_namespace/aaa/123/')
        assert res.status_code == 200

        text = 'Example of a detail view'
        self.assertContains(res, text, count = 3, html=False)

        text = 'Arg from view: 123'
        self.assertContains(res, text, count = 1, html=False)

    def test_sub1_with_ns_and_pk_as_template(self):
        res = self.client.get('/test1_namespace/bbb/321/')
        assert res.status_code == 200

        # simple inclusion doesn't treat mappings as templates
        text = 'Example of a detail view with pk: {{ pk }}'
        self.assertContains(res, text, count = 1, html=False)

        # but rendering breadcrumbs as a templatetag does
        text = 'Example of a detail view with pk: 321'
        self.assertContains(res, text, count = 2, html=False)

        text = 'Arg from view: 321'
        self.assertContains(res, text, count = 1, html=False)

    def test_sub1_with_ns_and_pk_as_template_verbose_name(self):
        res = self.client.get('/test1/ccc/111/')
        assert res.status_code == 200

        # simple inclusion doesn't treat mappings as templates
        text = 'Test1 subpage via custom url with context var {{ pk }}'
        self.assertContains(res, text, count = 1, html=False)

        # but rendering breadcrumbs as a templatetag does
        text = 'Test1 subpage via custom url with context var 111'
        self.assertContains(res, text, count = 2, html=False)

        text = 'Arg from view: 111'
        self.assertContains(res, text, count = 1, html=False)

    def test_url_without_a_trailing_slash(self):
        res = self.client.get('/test1/ddd/555')
        assert res.status_code == 200

        # simple inclusion doesn't treat mappings as templates
        text = 'Example of a detail view without a trailing slash with pk: {{ pk }}'
        self.assertContains(res, text, count = 1, html=False)

        # but rendering breadcrumbs as a templatetag does
        text = 'Example of a detail view without a trailing slash with pk: 555'
        self.assertContains(res, text, count = 2, html=False)

    def test_url(self):
        res = self.client.get('/test1/aaa/')
        assert res.status_code == 200

        text = 'Test1 subpage via custom url function'
        self.assertContains(res, text, count = 3, html=False)
