#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            'id', 'username', 'password', 'email', 'first_name', 'last_name'
        ]
