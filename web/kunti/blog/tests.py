from unittest import mock

from django.contrib.auth import models as auth_models
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog import models


class TestPost(APITestCase):

    def setUp(self):
        self._create_dummy_records()

    def _construct_expected_published_date(self, published_date):
        expected_published_date = published_date.replace(" ", "T")
        expected_published_date += 'Z'
        return expected_published_date

    def _create_dummy_records(self):
        self._create_dummy_author()
        self._create_dummy_posts()

    def _create_dummy_author(self):
        self.abhilash = auth_models.User.objects.create(
            username="abhilash",
            password="12345",
            email="abhilash@gmail.com",
            first_name="Abhilash",
            last_name="Sharma"
        )

    def _create_dummy_posts(self):
        self.posts_data = [
            {
                "title": "Thanks Mahendra Singh Dhoni!",
                "body": "I love Mahendra Singh Dhoni. He is great batsman.",
                "published_date": "2019-07-27 19:14:19.872839"
            },
            {
                "title": "Event report Pycon Australia 2019",
                "body": "Pycon Australia 2019 was a great event",
                "published_date": "2019-08-27 19:14:19.872839"
            }
        ]
        self.posts = []
        for post_data in self.posts_data:
            with mock.patch("django.utils.timezone.now") as mocked_datetime:
                mocked_datetime.return_value = post_data['published_date']
                post = models.Post.objects.create(
                    author=self.abhilash,
                    title=post_data['title'],
                    body=post_data['body']
                )
                self.posts.append(post)

    def _serialize_post(self, post):
        expected_published_date = self._construct_expected_published_date(
            post.published_date
        )
        serialized_post = {
            "id": post.id,
            "published_date": expected_published_date,
            "author": self.abhilash.id,
            "title": post.title,
            "body": post.body,
        }
        return serialized_post

    def test_that_it_is_possible_to_get_a_post(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = self._serialize_post(self.posts[0])
        self.assertDictEqual(response.data, expected_data)

    def test_that_it_is_possible_to_get_list_of_posts(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = []
        for post in self.posts:
            serialized_post = self._serialize_post(post)
            expected_data.append(serialized_post)
        self.assertListEqual(response.data, expected_data)

    def test_that_it_is_possible_to_create_new_post(self):
        new_post = {
            "author": self.abhilash.id,
            "title": "How to write data capturing tool?",
            "body": (
                "I think you are interested in writing a data capturing tool."
            ),
        }
        response = self.client.post('/posts/', new_post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        is_post_created = models.Post.objects.filter(
            title=new_post['title'],
            body=new_post['body'],
            author=self.abhilash.id
        ).exists()
        self.assertTrue(is_post_created)

    def test_that_it_is_possible_to_update_existing_post(self):
        updated_post = {
            'title': 'Thanks Rahul dravid!',
            'body': 'I love Rahul dravid. He is good batsman.',
        }
        response = self.client.patch('/posts/1/', updated_post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        is_post_updated = models.Post.objects.filter(
            title=updated_post['title'],
            body=updated_post['body']
        ).exists()
        self.assertTrue(is_post_updated)
        number_of_posts = models.Post.objects.count()
        self.assertEqual(number_of_posts, len(self.posts))

    def test_that_it_is_possible_to_delete_existing_post(self):
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        number_of_posts = models.Post.objects.count()
        expected_number_of_posts = len(self.posts) - 1
        self.assertEqual(number_of_posts, expected_number_of_posts)
