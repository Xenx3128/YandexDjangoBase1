from django.test import Client, TestCase
from django.urls import reverse


class TaskPagesTest(TestCase):
    def test_catalog_item_list_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertIn('app_name', response.context)
