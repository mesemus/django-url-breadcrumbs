#encoding: utf-8

from django.test import SimpleTestCase
# from urlbreadcrumbs.tests.views import index

class BreadcrumbsTest(SimpleTestCase):

    def test_index(self):
        res = self.client.get('/')
        assert res.status_code == 200

        text = "A title for a home page"
        self.assertContains(res, text, count = 3, html=False)

    def test_sub1(self):
        res = self.client.get('/test1/')
        assert res.status_code == 200

        text = "Index page of Test1"
        self.assertContains(res, text, count = 3, html=False)
