from django.db.models import Min, Q
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
    queryset = models.Product.objects.annotate(
        min_amount=Min('seller_products__amount', filter=Q(seller_products__is_active=True))
    )

    # annotate(
    #     min_amount=Min('seller_products__amount', filter=Q(seller_products__is_active=True))
    # )

    # def get_permissions(self):
    #     if self.action in ('list', 'retrieve'):
    #         return IsAuthenticated(),
    #     return permissions.IsMe(),
    #
    #     return permissions.IsMe(),


class ProductImageViewSet(ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.select_related('product')
