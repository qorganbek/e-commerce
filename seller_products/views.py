from rest_framework.viewsets import ModelViewSet
from . import models, serializers, permissions
from utils import mixins


class SellerProductView(mixins.ActionSerializerMixin,
                        mixins.ActionPermissionMixin,
                        ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreateSellerProductSerializer,
        'update': serializers.UpdateSellerProductSerializer,
        'partial_update': serializers.UpdateSellerProductSerializer
    }

    ACTION_PERMISSIONS = {
        'update': (permissions.IsSellerAndOwner(),),
        'partial_update': (permissions.IsSellerAndOwner(),),
        'destroy': (permissions.IsSellerAndOwner(),)
    }

    queryset = models.SellerProduct.objects.select_related('product', 'seller')
    serializer_class = serializers.SellerProductSerializer
    permission_classes = permissions.IsSellerOrReadOnly,

    # def perform_create(self, serializer):
    #     serializer.save(seller=self.request.user)


'''
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMTkzOTQ4LCJqdGkiOiIyYTMyZTk3MmQ4MGY0ZGViODE3ZjJhMjEwNTc5ZjEwYyIsInVzZXJfaWQiOiI5YTkxYTUzMS03YTQ4LTQyMjgtOTg0Ni00OWNjZDc3MjhlOGMifQ.9Voq686QcGVLlPKrRsYNY8fiGreDFsVGW3XjB1Q6uuU",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MTI2MjM0OCwianRpIjoiZDVmNDBlNjRkMmU2NDk4Nzg0ZjNiMDQwZWJiYjE4ZmEiLCJ1c2VyX2lkIjoiOWE5MWE1MzEtN2E0OC00MjI4LTk4NDYtNDljY2Q3NzI4ZThjIn0.wFJ1UX-qdtYQSA5jGnrOSy2VVdMxDD0a4ZpnVXseY-I"
}
'''
