from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели комментария"""
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'date_posted', 'date_modified', 'post']
        read_only_fields = ['date_posted', 'date_modified', 'author', 'post']


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели публикации"""
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'date_posted', 'date_modified', 'comments']
        read_only_fields = ['date_posted', 'date_modified', 'author', 'comments']
