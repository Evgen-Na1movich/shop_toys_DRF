from django_filters import rest_framework as filters

from toys.models import Toy


class ToysFilter(filters.FilterSet):
    """Фильтр для игрушек по категориям."""

    categories = filters.CharFilter(lookup_expr='icontains')
    brend = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Toy
        fields = ('categories', 'brend',)
