from django.contrib.auth.models import User
from rest_framework import serializers

from toys.models import Toy, Brend, Category, Item, Order


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
    """Serializer для заказа."""

    creator = UserSerializer(read_only=True)
    positions = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'creator', 'positions', 'status', 'total_price', 'created_at', 'updated_at',)

    def create(self, validated_data):
        """Метод создания заказа"""
        validated_data["creator"] = self.context["request"].user
        positions_data = validated_data.pop('positions')
        order = super().create(validated_data)
        order.save()
        raw_positions = []
        for position in positions_data:
            position = Item(order=order,
                            product=position["product"],
                            quantity=position["quantity"],
                            price=position["product"].price)
            raw_positions.append(position)
        Item.objects.bulk_create(raw_positions)
        return order

    def update(self, instance, validated_data):
        """Метод для обновления"""
        order = Order.objects.get(pk=instance.id)
        if order.status != validated_data['status'] and not self.context["request"].user.is_staff:
            raise serializers.ValidationError("Only admin can update status")
        return super().update(instance, validated_data)