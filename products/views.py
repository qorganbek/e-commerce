from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from utils import mixins
from . import serializers, models, permissions


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return serializers.RetrieveProductSerializer
    #
    #     return serializers.ProductSerializer

    serializer_class = serializers.ProductSerializer
    # permission_classes = (IsAuthenticated,)
    queryset = models.Product.objects.prefetch_related('product_images')

    # def get_permissions(self):
    #     if self.action in ('list', 'retrieve'):
    #         return IsAuthenticated(),
    #     return permissions.IsMe(),
    #
    #     return permissions.IsMe(),


class ProductImageViewSet(ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.select_related('product')
