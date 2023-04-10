from rest_framework import serializers
from . import models
from products.serializers import ProductSerializer


class SellerProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = models.SellerProduct
        fields = '__all__'
