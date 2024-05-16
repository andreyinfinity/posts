from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class OtherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_name']
