from django.contrib.auth import models as auth_models
from django.db import models


class Post(models.Model):

    author = models.ForeignKey(
        auth_models.User,
        on_delete=models.PROTECT
    )
    published_date = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=100)
    body = models.TextField(max_length=140, blank=True)


class Comment(models.Model):

    author = models.ForeignKey(
        auth_models.User,
        on_delete=models.PROTECT
    )
    created_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT
    )
    body = models.TextField(max_length=80)
