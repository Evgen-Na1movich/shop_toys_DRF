from django.contrib.auth.models import User
from rest_framework import serializers

from toys.models import Toy, Brend, Category


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class CategorySerializer(serializers.ModelSerializer):
    """Serializer для категорий"""

    class Meta:
        model = Category
        fields = ('id', 'name')


class BrendSerializer(serializers.ModelSerializer):
    """Serializer для бренда"""

    class Meta:
        model = Brend
        fields = ('brend',)


class ToySerializer(serializers.ModelSerializer):
    """Serializer для товара(игрушек)"""
    categories = CategorySerializer(many=True)

    class Meta:
        model = Toy
        fields = '__all__'
