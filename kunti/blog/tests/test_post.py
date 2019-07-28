from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from blog import models
from . import dummy
from . import mocks


class TestPost(APITestCase):

    def setUp(self):
        self._create_dummy_records()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )

    def _create_dummy_records(self):
        self.author = dummy.create_author()
        self.posts = [
            dummy.create_post(self.author),
            dummy.create_post(self.author)
        ]
        self.token = Token.objects.create(user=self.author)

    def _serialize_post(self, post):
        serialized_post = {
            "id": post.id,
            "published_date": mocks.MockedDateTime.timezoned,
            "author": self.author.id,
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
            "author": self.author.id,
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
            author=self.author.id
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
