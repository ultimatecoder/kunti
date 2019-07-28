#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import include, path

from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from blog import views


schema_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        default_version='v1'
    ),
)

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'docs', schema_view.with_ui('swagger')),
]
