from django.test import Client, TestCase


class StaticURLTest(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_wrong_address(self):
        response = Client().get('home/')
        self.assertEqual(response.status_code, 404)
