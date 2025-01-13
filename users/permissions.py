from rest_framework import permissions


class IsCreater(permissions.BasePermission):
    """Проверка на создателя объекта."""

    def has_object_permission(self, request, view, obj):
        return obj.creater == request.user