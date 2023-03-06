from django.test import Client
from django.test import TestCase
from faker import Faker

from .models import BlogUser


class ViewsTestUser(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.post('/users/register/', {'username': self.fake.name(), 'password': 'smith'})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/users/login/', {'username': self.fake.name(), 'password': 'smith'})
        self.assertEqual(response.status_code, 200)

