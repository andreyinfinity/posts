from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.permissions import IsAdmin, IsSelf
from users.serializers import UserSerializer


class UserRegister(generics.CreateAPIView):
    """Создание нового пользователя"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Шифрование пароля перед записью в БД"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieve(generics.RetrieveAPIView):
    """Отображение пользователя"""
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserList(generics.ListAPIView):
    """Отображение списка пользователей"""
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdate(generics.UpdateAPIView):
    """Редактирование пользователя"""
    permission_classes = [IsSelf, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        """Шифрование пароля перед записью в БД"""
        user = serializer.save(is_active=True)
        if serializer.data.get('password'):
            user.set_password(user.password)
        user.save()


class UserDelete(generics.DestroyAPIView):
    """Удаление пользователя"""
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
