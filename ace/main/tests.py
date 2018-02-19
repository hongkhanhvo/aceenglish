from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import base

class BaseTests(TestCase):
    def test_base_view_status_code(self):
        url = reverse('base')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_base_url_resolves_base_view(self):
        view = resolve('/')
        self.assertEquals(view.func, base)
