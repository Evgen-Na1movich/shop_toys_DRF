from django_filters import rest_framework as filters

from toys.models import Toy


class ToysFilter(filters.FilterSet):
    """Фильтр для игрушек по категориям."""
    price_from = filters.NumberFilter(field_name='price', lookup_expr="gte")
    price_to = filters.NumberFilter(field_name='price', lookup_expr="lte")
    name = filters.CharFilter(lookup_expr='icontains')
    brend = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Toy
        fields = ('price_from', 'price_to', 'name', 'brend',)


class OrderFilter(filters.FilterSet):
    pass