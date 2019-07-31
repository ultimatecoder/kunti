from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from blog import serializers, models, permissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrReadOnly)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrReadOnly)
