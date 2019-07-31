from django.contrib.auth import models
from rest_framework import mixins, viewsets

from user import serializers


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
