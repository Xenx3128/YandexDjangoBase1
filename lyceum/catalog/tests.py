from catalog.models import Category, Item, Tag
from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTest(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_wrong_address(self):
        response = Client().get('/catalogs/')
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


class TaskPagesTest(TestCase):
    def test_catalog_item_list_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertIn('app_name', response.context)
