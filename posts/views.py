from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from users.permissions import IsAuthor, IsAdmin


class PostViewSet(viewsets.ModelViewSet):
    """CRUD для публикаций"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # pagination_class = PostPaginator

    def perform_create(self, serializer):
        """Метод для добавления пользователя при создании публикации"""
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """
        Метод для определения прав доступа:
        - создание объекта доступно авторизованному пользователю;
        - просмотр объекта доступен всем;
        - редактирование и удаление объекта доступно автору или администратору.
        """
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthor | IsAdmin]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    """CRUD для комментариев"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # pagination_class = PostPaginator

    def get_post(self):
        """Возвращает объект текущей публикации"""
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        """Возвращает queryset c комментариями для текущей публикации"""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """
        Метод для добавления текущего поста и
        текущего пользователя при создании комментария
        """
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def get_permissions(self):
        """
        Метод для определения прав доступа:
        - создание объекта доступно авторизованному пользователю;
        - просмотр объекта доступен всем;
        - редактирование и удаление объекта доступно автору или администратору.
        """
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthor | IsAdmin]
        return [permission() for permission in permission_classes]
