from dataclasses import field
from rest_framework import serializers

from app.models import Comment, Post, Image


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')


class SetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')
