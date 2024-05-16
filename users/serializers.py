from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth']
        write_only_fields = ['password']


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации нового пользователя"""
    class Meta:
        model = User
        fields = ['username', 'password']
        write_only_fields = ['password']

    def to_representation(self, instance):
        return {'username': instance.username}
