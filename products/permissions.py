from rest_framework.permissions import DjangoObjectPermissions
from . import models


class IsMe(DjangoObjectPermissions):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.email == 'extra@gmail.com')

    def has_object_permission(self, request, view, obj: models.Product):
        # print(request.user, obj.user)
        return obj.user == request.user
