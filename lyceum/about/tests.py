from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTest(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_wrong_address(self):
        response = Client().get('/about_us/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
