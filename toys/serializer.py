from django.contrib.auth.models import User
from rest_framework import serializers

from toys.models import Toy, Brend, Category, Item


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class CategorySerializer(serializers.ModelSerializer):
    """Serializer для категорий."""

    # Вместо id возвращается строковое представление объекта.
    toys_by_category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'toys_by_category')


class BrendSerializer(serializers.ModelSerializer):
    """Serializer для бренда."""

    # Вместо id возвращается строковое представление объекта.
    toys_by_brend = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Brend
        fields = ('name', 'toys_by_brend')


class ToySerializer(serializers.ModelSerializer):
    """Serializer для товара(игрушек)."""
    categories = CategorySerializer(many=True)
    brend = serializers.StringRelatedField()

    class Meta:
        model = Toy
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    """Serializer для позиции."""
    product = serializers.PrimaryKeyRelatedField(
        queryset=Toy.objects.all(),
        required=True)

    class Meta:
        model = Item
        fields = ('product', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    pass
