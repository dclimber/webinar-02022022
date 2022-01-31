from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found_view = resolve('/')

        self.assertEqual(found_view.func, home_page)
        self.assertEqual(found_view.url_name, 'home')
        self.assertEqual(found_view.app_name, 'pages')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Портфолио Декса</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
