from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.viewsets import ModelViewSet

from toys.models import Toy, Brend, Category
from toys.serializer import ToySerializer, BrendSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrendViewSet(ModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class ToyViewSet(ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
