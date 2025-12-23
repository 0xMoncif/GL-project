from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "user_type", "created_at"]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    # maybe i will add confirm password later
    class Meta:
        model = User
        fields = ["email", "password", "user_type"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
