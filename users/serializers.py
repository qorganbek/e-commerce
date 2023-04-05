from rest_framework import serializers
from . import models
from phonenumber_field import serializerfields


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('phone_number', 'email')


class CreateTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class GetUserSerializer(serializers.Serializer):
    token = serializers.CharField()


class VerifyUserSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    code = serializers.CharField(max_length=4)
