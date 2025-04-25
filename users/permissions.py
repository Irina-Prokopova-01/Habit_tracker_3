from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    """Проверка на создателя объекта."""

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
