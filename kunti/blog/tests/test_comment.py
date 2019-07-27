#! /usr/bin/env python

from rest_framework import status
from rest_framework.test import APITestCase

from . import dummy


class TestComment(APITestCase):

    def setUp(self):
        self._create_dummy_records()

    def _create_dummy_records(self):
        self.author = dummy.create_author()
        self.post = dummy.create_post(self.author)
        self.comment = dummy.create_comment(self.author, self.post)

    def test_that_it_is_possible_to_read_a_comment(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
