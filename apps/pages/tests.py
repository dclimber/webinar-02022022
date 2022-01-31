from django.test import TestCase
from django.urls import resolve

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found_view = resolve('/')

        self.assertEqual(found_view.func, home_page)
        self.assertEqual(found_view.url_name, 'home')
