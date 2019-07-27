from unittest import mock

from django.contrib.auth import models as auth_models
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog import models


class TestPost(APITestCase):

    def _construct_expected_published_date(self, published_date):
        expected_published_date = published_date.replace(" ", "T")
        expected_published_date += 'Z'
        return expected_published_date

    def test_that_it_is_possible_to_get_an_instance_of_post(self):
        published_date = "2019-07-27 19:14:19.872839"
        with mock.patch("django.utils.timezone.now") as mocked_datetime:
            mocked_datetime.return_value = published_date
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
        response = self.client.get('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_published_date = self._construct_expected_published_date(
            published_date
        )
        self.assertEqual(response.data, {
            "id": post.id,
            "published_date": expected_published_date,
            "author": abhilash.id,
            "title": post.title,
            "body": post.body,
        })
