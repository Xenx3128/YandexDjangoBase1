from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTest(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_wrong_address(self):
        response = Client().get('home/')
        self.assertEqual(response.status_code, 404)


class TaskPagesTest(TestCase):
    def test_home_page_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertIn('app_name', response.context)
