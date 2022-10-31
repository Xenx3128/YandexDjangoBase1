from django.test import Client, TestCase
from django.core.exceptions import ValidationError

from catalog.models import Item, Category, Tag


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


class ModelsTest(TestCase):
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

    def test_item_incorrect(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(name='Test item',
                             category=self.category,
                             text='Sample text')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_item_upper_case_correct(self):
        item_count = Item.objects.count()
        self.item = Item(name='Test item',
                         category=self.category,
                         text='Sample text Превосходно')
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_item_lower_case_correct(self):
        item_count = Item.objects.count()
        self.item = Item(name='Test item',
                         category=self.category,
                         text='Sample text роскошно')
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)
