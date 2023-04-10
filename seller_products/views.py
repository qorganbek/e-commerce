from rest_framework import viewsets
from . import  models, serializers


class SellerProductView(viewsets.ModelViewSet):
    queryset = models.SellerProduct.objects.select_related('product', 'seller')
    serializer_class = serializers.SellerProductSerializer

