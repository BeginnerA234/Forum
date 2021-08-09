from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrStaffOrReadOnly(BasePermission):
    """
    См.название класса
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            (obj.id == request.user.id or request.user.is_staff)
        )


class IsAuthenticateAndIsOwner(BasePermission):
    """
    GET запросы разрешен только стафу
    POST запросы принимаются только от пользователей,
    при условии, что они игнорируют пользователей для себя.
    Принимает по одному объекту!
    PUT,PATCH только для владельцев
    """

    def has_permission(self, request, view):
        """
        if request.data: POST
        else: GET
        """
        if request.data:

            return bool(
                request.user and
                request.user.is_authenticated and
                (view.request.user.id == int(request.data.get('user', 0)))
            )
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        """PUT/PATCH"""
        return bool(
            request.user.is_authenticated and
            obj.user == request.user
        )
