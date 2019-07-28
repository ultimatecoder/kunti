#! /usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import mock

from django.contrib.auth import models

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestUser(APITestCase):

    def setUp(self):
        self.user = models.User.objects.create_user(
            "gandhari", "123456", "gandhari@gmail.com"
        )
        self.user.save()

    def test_that_it_is_possible_to_get_token(self):
        with mock.patch(
            "rest_framework.authtoken.serializers.authenticate"
        ) as mocked_authenticate:
            mocked_authenticate.return_value = self.user
            response = self.client.post("/token/", {
                'username': self.user.username,
                'password': self.user.password
            })
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = Token.objects.all()[0]
        self.assertDictEqual(response.data, {"token": token.key})

    def test_that_getting_token_is_not_possible_with_wrong_details(self):
        response = self.client.post("/token/", {
            'username': 'random-user',
            'password': 'i am pass'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
