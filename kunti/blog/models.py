from django.conf import settings
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
