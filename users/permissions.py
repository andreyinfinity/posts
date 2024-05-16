from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Проверка является ли пользователь администратором"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()


class IsAuthor(BasePermission):
    """Проверка является ли пользователь автором"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsSelf(BasePermission):
    """Проверка является ли пользователь сам собой"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj
