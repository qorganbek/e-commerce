import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), is_active=True)
        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, phone_number, email, password=None):
        user = self.create_user(
            phone_number=phone_number,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def active(self):
        return self.filter(is_active=True)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(blank=True, null=True, max_length=1)
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone_number)


# tokens access and refresh
