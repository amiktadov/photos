from dataclasses import field
from rest_framework.serializers import ModelSerializer as MS

from app.models import Comment, Post, Image, Reaction


class CommentSerializer(MS):
    class Meta:
        model = Comment
        fields = "__all__"


class ReactionSerializer(MS):
    class Meta:
        model = Reaction
        fields = "__all__"


class PostSerializer(MS):
    reactions = ReactionSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

