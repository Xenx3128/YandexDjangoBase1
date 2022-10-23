from django.test import Client, TestCase


class StaticURLTest(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_wrong_address(self):
        response = Client().get('/catalogs/')
        self.assertEqual(response.status_code, 404)


class ItemRegexTest(TestCase):
    def test_catalog_item_endpoint(self):
        response = Client().get('/catalog/1')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_multiple_num_endpoint(self):
        response = Client().get('/catalog/100')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_wrong_address(self):
        response = Client().get('/catalogs/1')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_negative_number(self):
        response = Client().get('/catalog/-12')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_letters(self):
        response = Client().get('/catalog/abc')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_numbers_with_letters(self):
        response = Client().get('/catalog/123abc')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_mixed_letters(self):
        response = Client().get('/catalog/1a2b3c')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_zero(self):
        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_mixed_characters(self):
        response = Client().get('/catalog/123_456')
        self.assertEqual(response.status_code, 404)
