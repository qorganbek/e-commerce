from django.contrib.auth import get_user_model
from django.db import models
from users import choices as user_choices
from . import choices as amount_choices


class SellerProduct(models.Model):
    product = models.ForeignKey(to='products.Product', on_delete=models.PROTECT, related_name='seller_products')
    seller = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='seller_products',
        limit_choices_to={'user_type': user_choices.UserType.Seller}
    )
    is_active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    amount_currency = models.CharField(max_length=3, choices=amount_choices.CurrencyChoices.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
