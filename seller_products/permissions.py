from rest_framework import permissions
from users import choices as user_choices


class IsSellerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user
            and request.user.is_authenticated
            and request.user.user_type == user_choices.UserType.Seller
        )


class IsSellerAndOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.user_type == user_choices.UserType.Seller
        )

    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user

