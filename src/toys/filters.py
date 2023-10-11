from django_filters import rest_framework as filters

from toys.models import Toy, Order, OrderStatusChoices


class ToysFilter(filters.FilterSet):
    """Фильтр для игрушек по категориям."""
    price_from = filters.NumberFilter(field_name='price', lookup_expr="gte")  # фильтрация по 'price'.Больше или равно
    price_to = filters.NumberFilter(field_name='price', lookup_expr="lte")  # Меньше или равно.
    name = filters.CharFilter(lookup_expr='icontains')  # Тест содержания без учета регистра.
    brend = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Toy
        fields = ('price_from', 'price_to', 'name', 'brend',)


class OrderFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=OrderStatusChoices.choices)
    price_from = filters.NumberFilter(field_name='total_price', lookup_expr="gte")
    price_to = filters.NumberFilter(field_name='total_price', lookup_expr="lte")
    products = filters.CharFilter()
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Order

        fields = ('status', 'price_from', 'price_to', 'products', 'created_at', 'updated_at',)