from django.contrib.auth.models import User
from django.db.models.functions import datetime
from rest_framework import serializers
from rest_framework.response import Response

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
    # categories = CategorySerializer(many=True)
    brend = serializers.StringRelatedField()

    class Meta:
        model = Toy
        fields = ('name', 'price', 'brend', 'discription',)

    # def create(self, validated_data):
    #     now = datetime.datetime.now()
    #     hour_now = now.hour
    #     if 8 < hour_now < 12:
    #         return Toy(**validated_data)
    #     else:
    #         return Response({'message': 'пшел вон, я сплю'})


class ItemSerializer(serializers.ModelSerializer):
    """Serializer для позиции."""
    # этот тип поля в сериализаторе оперирует первичными ключами (id) связанного объекта
    # Когда добавляем игрушку в позицию, то указываем ее id
    product = serializers.PrimaryKeyRelatedField(
        queryset=Toy.objects.all(),
        required=False)

    # print(f'product - {product}')

    class Meta:
        model = Item
        fields = ('product', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    """Serializer для заказа."""

    creator = UserSerializer(read_only=True, required=False)
    positions = ItemSerializer(many=True, required=False, default=None)

    class Meta:
        model = Order
        fields = ('id', 'creator', 'positions', 'status', 'total_price', 'created_at', 'updated_at', 'adress',)
    def create(self, validated_data):

        #     """Метод создания заказа"""
        validated_data["creator"] = self.context["request"].user
        positions_data = validated_data.pop('positions')
        order = Order.objects.create(**validated_data)
        order.save()
        # for positions_data in positions_data:
        #     Item.objects.create(order=order, **positions_data)
        raw_positions = []
        for position in positions_data:
            print(f'position - {position}')
            position = Item(order=order,
                            product=position["product"],
                            quantity=position["quantity"],
                            price=position["product"].price)
            raw_positions.append(position)
            print(raw_positions)
        Item.objects.bulk_create(raw_positions)
        return order

    def update(self, instance, validated_data):
        """Метод для обновления"""
        order = Order.objects.get(pk=instance.id)
        if order.status != validated_data['status'] and not self.context["request"].user.is_staff:
            raise serializers.ValidationError("Only admin can update status")
        return super().update(instance, validated_data)
