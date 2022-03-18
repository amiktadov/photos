from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from app.models import Post, Image, Reaction, Size, Comment
from app.serializers import PostSerializer, CommentSerializer, ReactionSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
