#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from blog import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
