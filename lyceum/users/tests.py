import datetime


from http import HTTPStatus

from django.test import Client, TestCase

from .models import User
from django.urls import reverse


class ContextProcessorTest(TestCase):
                                     
    def test_processor_correct(self):
        User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345',
            birthday=datetime.date.today())
        response = self.client.get(reverse('homepage:home'))
        self.assertEqual(response.context[0]['birth_users'], )

    def test_catalog_wrong_address(self):
        response = Client().get('/catalogs/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
