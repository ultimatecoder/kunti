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

    def test_that_user_is_able_to_signup(self):
        user = {
            "username": "abhilash",
            "password": "12345",
            "email": "abhilash@gmail.com",
            "first_name": "Abhilash",
            "last_name": "Sharma"
        }
        response = self.client.post("/signup/", user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        is_user_created = models.User.objects.filter(
            username=user['username'],
            email=user['email'],
            first_name=user['first_name'],
            last_name=user['last_name']
        )
        self.assertTrue(is_user_created)

    def test_that_user_is_able_to_login_when_details_are_correct(self):
        with mock.patch(
            "rest_framework.authtoken.serializers.authenticate"
        ) as mocked_authenticate:
            mocked_authenticate.return_value = self.user
            response = self.client.post("/login/", {
                'username': self.user.username,
                'password': self.user.password
            })
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = Token.objects.all()[0]
        self.assertDictEqual(response.data, {"token": token.key})

    def test_that_user_not_able_to_login_when_details_are_wrong(self):
        response = self.client.post("/login/", {
            'username': 'random-user',
            'password': 'i am pass'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
