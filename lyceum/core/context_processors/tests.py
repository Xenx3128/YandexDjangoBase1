from http import HTTPStatus

from django.test import Client, TestCase

from .age import birthdays


class ContextProcessorTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(is_published=True,
                                               name="TestCategoryName",
                                               slug='test-category-slug',
                                               weight=100)
        cls.tag = Tag.objects.create(is_published=True,
                                     name="TestTag",
                                     slug="test-tag-slug")

                                     
    def test_processor_correct(self):
        response = Client().get('/')
        list = 
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_wrong_address(self):
        response = Client().get('/catalogs/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
