from rest_framework import serializers
from . import models
from products.serializers import ProductSerializer


class CreateSellerProductSerializer(serializers.ModelSerializer):
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.SellerProduct
        fields = (
            'seller',
            'product',
            'amount',
            'amount_currency',
            'is_active'
        )


class SellerProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = models.SellerProduct
        fields = '__all__'


class UpdateSellerProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SellerProduct
        fields = (
            'amount',
            'amount_currency',
            'is_active'
        )
