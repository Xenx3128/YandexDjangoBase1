from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTest(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_wrong_address(self):
        response = Client().get('/catalogs/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
