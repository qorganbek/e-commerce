from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from src import settings
from . import models
from users import choices

User = get_user_model()


@receiver(signals.post_save, sender=models.Product)
def send_email_to_seller(sender, instance: models.Product, created: bool, **kwargs):
    if created:
        sellers = User.objects.filter(user_type=choices.UserType.Seller)
        emails = [i.email for i in sellers]

        send_mail(
                f'new product {instance.title}',
                f'info: {instance.body}',
                settings.EMAIL_HOST_USER,
                emails
        )

