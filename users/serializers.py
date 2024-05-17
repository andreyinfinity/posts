from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth']

    def validate_email(self, value):
        if value:
            if 'mail.ru' not in value.lower() and 'yandex.ru' not in value.lower():
                raise serializers.ValidationError("Можно добавлять почту только mail.ru или yandex.ru")
        return value


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации нового пользователя"""
    class Meta:
        model = User
        fields = ['username', 'password']
        write_only_fields = ['password']

    def validate_password(self, value):
        if len(value) > 8 and any(char.isdigit() for char in value):
            return value
        raise serializers.ValidationError("Пароль должен быть не менее 8 символов и включать цифры")

    def to_representation(self, instance):
        return {'username': instance.username}
