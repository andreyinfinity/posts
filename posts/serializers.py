from datetime import datetime

from rest_framework import serializers
from posts.models import Post, Comment


forbidden_words = ['ерунда', 'глупость', 'чепуха']


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

    def validate_title(self, value):
        for word in forbidden_words:
            if word.lower() in value.lower():
                raise serializers.ValidationError(f"Слово '{word}' запрещено использовать в заголовке")
        return value

    def validate(self, attrs):
        today = datetime.now().date()
        birth = self.context['request'].user.date_of_birth
        if birth:
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            if age < 18:
                raise serializers.ValidationError("Писать публикации разрешено с 18 лет")
            return attrs
        raise serializers.ValidationError("Заполните поле дата рождения в своем профиле")
