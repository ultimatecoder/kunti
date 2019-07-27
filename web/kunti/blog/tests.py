from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase


class TestBlog(APITestCase):

    def test_that_it_is_possible_to_get_an_instance_of_blog(self):
        response = self.client.get('blog/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
