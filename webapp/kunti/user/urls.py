#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from user import views


router = DefaultRouter()
router.register(r'users', views.UserCreateViewSet)


urlpatterns = [
    path(r'login/', obtain_auth_token),
    path('', include(router.urls)),
]
