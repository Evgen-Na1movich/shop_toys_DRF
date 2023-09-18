from django.contrib.auth.models import User
from rest_framework import serializers

from toys.models import Toy, Brend, Category, ToyCategory, Item


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class CategorySerializer(serializers.ModelSerializer):
    """Serializer для категорий."""

    # Вместо id возвращается строковое представление объекта.
    # toys_by_category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name')


class BrendSerializer(serializers.ModelSerializer):
    """Serializer для бренда."""

    # Вместо id возвращается строковое представление объекта.
    # toys_by_brend = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Brend
        fields = ('name', 'toys_by_brend')


class ToySerializer(serializers.ModelSerializer):
    """Serializer для товара(игрушек)."""
    categories = CategorySerializer(many=True)

    # brend = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Toy
        fields = ('name', 'brend', 'price', 'categories', 'gender',)

    def create(self, validated_data):
        # Уберем список категорий из словаря validated_data и сохраним его
        categories = validated_data.pop('categories')
        # создаем новую игрушку без категории
        toy = Toy.objects.create(**validated_data)

        # Для каждой категории из списка категорий
        for category in categories:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_categories, status = Category.objects.get_or_create(
                **categories)
            # Поместим ссылку на каждую категорию во вспомогательную таблицу
            # Не забыв указать к какой игрушке оно относится
            Toy.objects.create(
                category=current_categories, toy=toy)
        return toy


class ItemSerializer(serializers.ModelSerializer):
    """Serializer для позиции."""

    product = serializers.PrimaryKeyRelatedField(
        queryset=Toy.objects.all(),
        required=True)

    class Meta:
        model = Item
        fields = ('product', 'quantity',)
