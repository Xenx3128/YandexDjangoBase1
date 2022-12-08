import datetime

from django.test import TestCase
from django.urls import reverse

from .models import User


class ContextProcessorTest(TestCase):
    def test_processor_correct(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345',
            birthday=datetime.date.today())
        response = self.client.get(reverse('homepage:home'))
        self.assertEqual(len(response.context['birth_users']), 1)
        self.assertEqual(list(response.context['birth_users']), [user])

    def test_processor_diff_url(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345',
            birthday=datetime.date.today())
        response = self.client.get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['birth_users']), 1)
        self.assertEqual(list(response.context['birth_users']), [user])

    def test_processor_diff_year(self):
        bday = datetime.date.today().replace(year=1945)
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345',
            birthday=bday)
        response = self.client.get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['birth_users']), 1)
        self.assertEqual(list(response.context['birth_users']), [user])

    def test_processor_no_bdays(self):
        bday = datetime.date.today() + datetime.timedelta(days=10)
        User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345',
            birthday=bday)
        response = self.client.get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['birth_users']), 0)
        self.assertEqual(list(response.context['birth_users']), [])

    def test_processor_multiple_bdays(self):
        users = []
        users.append(User.objects.create_user(
            username='testuser1',
            email='test@test.com',
            password='12345',
            birthday=datetime.date.today()))
        users.append(User.objects.create_user(
            username='testuser2',
            email='test2@test.com',
            password='123456',
            birthday=datetime.date.today()))
        response = self.client.get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['birth_users']), 2)
        self.assertEqual(list(response.context['birth_users']), users)

    def test_processor_some_bdays(self):
        users = []
        users.append(User.objects.create_user(
            username='testuser1',
            email='test@test.com',
            password='12345',
            birthday=datetime.date.today()))
        users.append(User.objects.create_user(
            username='testuser2',
            email='test2@test.com',
            password='123456',
            birthday=datetime.date.today()))
        bday = datetime.date.today() + datetime.timedelta(days=10)
        User.objects.create_user(
            username='testuser3',
            email='test3@test.com',
            password='12345',
            birthday=bday)
        response = self.client.get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['birth_users']), 2)
        self.assertEqual(list(response.context['birth_users']), users)
