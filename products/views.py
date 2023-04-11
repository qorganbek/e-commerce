from django.db.models import Min, Q
from rest_framework.viewsets import ModelViewSet
from utils import mixins
from . import serializers, models, permissions, services


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    product_service: services.ProductServicesInterface = services.ProductServicesV1()
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return serializers.RetrieveProductSerializer
    #
    #     return serializers.ProductSerializer

    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)
    queryset = product_service.get_products()

    # annotate(
    #     min_amount=Min('seller_products__amount', filter=Q(seller_products__is_active=True))
    # )

    # def get_permissions(self):
    #     if self.action in ('list', 'retrieve'):
    #         return IsAuthenticated(),
    #     return permissions.IsMe(),


class ProductImageViewSet(ModelViewSet):
    product_images_services: services.ProductImageServicesInterface = services.ProductImageServicesV1()
    serializer_class = serializers.ProductImageSerializer
    queryset = product_images_services.get_product_images()
    permission_classes = permissions.IsAdminOrReadOnly,
