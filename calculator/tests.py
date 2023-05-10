from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class Tests(TestCase):
    def test_add(self):
        response = self.client.get(reverse('add'), data={'a': 1, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 3})

    def test_divide(self):
        response = self.client.get(reverse('divide'), data={'a': 10, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 5})
