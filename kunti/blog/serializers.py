#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from blog import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id', 'author', 'title', 'body', 'published_date']
