from django.contrib.auth import get_user_model
from django.db import models
from users import choices as user_choices
from seller_products import choices as amount_choices
from . import choices as order_choices


class Order(models.Model):
    customer = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='orders',
        limit_choices_to={'user_type': user_choices.UserType.Customer}
    )

    status = models.CharField(
        max_length=25,
        choices=order_choices.OrderStatusChoices.choices,
        default=order_choices.OrderStatusChoices.New
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='order_item')
    seller_product = models.ForeignKey(
        to='seller_products.SellerProduct',
        on_delete=models.PROTECT,
        related_name='order_item',
        limit_choices_to={'is_active': True}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    amount = models.DecimalField(max_digits=14, decimal_places=2)
    amount_currency = models.CharField(max_length=3, choices=amount_choices.CurrencyChoices.choices)
