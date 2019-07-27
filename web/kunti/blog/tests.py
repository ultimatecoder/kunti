from django.contrib.auth import models as auth_models
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from blog import models


class TestPost(APITestCase):

    def test_that_it_is_possible_to_get_an_instance_of_post(self):
        abhilash = auth_models.User.objects.create(
            username="abhilash",
            password="12345",
            email="abhilash@gmail.com",
            first_name="Abhilash",
            last_name="Sharma"
        )
        post = models.Post.objects.create(
            author=abhilash,
            title="Thanks Mahendra Singh Dhoni!",
            body="I love Mahendra Singh Dhoni. He is great batsman."
        )
        response = self.client.get('post/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "author": abhilash.id,
            "title": post.title,
            "body": post.body,
        })
