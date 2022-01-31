from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve, reverse

from .views import home_page, thank_you


class ThankYouPageTest(TestCase):
    def test_url_resolves_to_thank_you_page_view(self):
        found_view = resolve('/thank-you/')

        self.assertEqual(found_view.func, thank_you)
        self.assertEqual(found_view.url_name, 'thank-you')
        self.assertEqual(found_view.app_name, 'pages')

    def test_uses_correct_template(self):
        response = self.client.get(reverse('pages:thank-you'))

        self.assertTemplateUsed(response, 'thank-you.html')


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found_view = resolve('/')

        self.assertEqual(found_view.func, home_page)
        self.assertEqual(found_view.url_name, 'home')
        self.assertEqual(found_view.app_name, 'pages')

    def test_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('<title>Портфолио Декса</title>', html)

    def test_uses_correct_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
