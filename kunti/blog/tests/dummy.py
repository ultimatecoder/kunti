#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates mock objects

This module creates an instance of desired class using static values
"""
from unittest import mock

from django.contrib.auth import models as auth_models
from blog import models
from . import mocks


def create_author():
    return auth_models.User.objects.create(
        username="abhilash",
        password="12345",
        email="abhilash@gmail.com",
        first_name="Abhilash",
        last_name="Sharma"
    )


def create_post(author):
    with mock.patch("django.utils.timezone.now", mocks.MockedDateTime):
        post = models.Post.objects.create(
            author=author,
            title="Thanks Mahendra Singh Dhoni!",
            body="I love Mahendra Singh Dhoni. He is great batsman.",
        )
    return post


def create_comment(author, post):
    with mock.patch("django.utils.timezone.now", mocks.MockedDateTime):
        comment = models.Comment.objects.create(
            author=author,
            post=post,
            body="Great post. Keep it up!"
        )
    return comment
