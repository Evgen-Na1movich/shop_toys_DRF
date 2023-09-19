from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, AllowAny

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


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []
