from django.test import Client, TestCase
from django.urls import reverse


class TaskPagesTest(TestCase):
    def test_home_page_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertIn('app_name', response.context)
