from django.contrib.auth.models import User
from rest_framework import serializers

from toys.models import Toy, Brend, Category


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class ToySerializer(serializers.ModelSerializer):
    """Serializer для товара(игрушек)"""
    class Meta:
        model = Toy
        fields = '__all__'


class BrendSerializer(serializers.ModelSerializer):
    """Serializer для бренда"""
    class Meta:
        model = Brend
        fields = ['brend']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer для категорий"""
    class Meta:
        model = Category
        fields = [
            'id', 'name'
        ]



