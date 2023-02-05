from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from utils import mixins
from . import serializers, models


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
    queryset = models.Product.objects.prefetch_related('product_images')


class ProductImageViewSet(ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.select_related('product')
