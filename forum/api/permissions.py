from rest_framework.permissions import BasePermission


class IsOwnerNotBlockedOrStaff(BasePermission):
    """
    GET запросы запрещены
    POST запросы принимаются только от активных пользователей,
    при условии, что они не заблокированы.
    Создать может только owner
    """

    def has_permission(self, request, view):
        """
        Создать может только owner
        creator - название поля в моделях
        """
        return bool(
            request.user and
            request.user.is_authenticated and
            not request.user.is_blocked and
            (int(request.data.get('creator', 0)) == request.user.id)
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            not request.user.is_blocked and
            (obj.user == request.user or request.user.is_staff)
        )
