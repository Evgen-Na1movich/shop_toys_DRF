from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from toys.filters import ToysFilter, OrderFilter
from toys.models import Toy, Brend, Category, Order
from toys.serializer import ToySerializer, BrendSerializer, CategorySerializer, OrderSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []


class BrendViewSet(ModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []


class ToyViewSet(ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filterset_class = ToysFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []


class IsOwnerOrAdmin(permissions.BasePermission):
    """Класс разрешений для владельца """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.creator == request.user


class OrderViewSet(ModelViewSet):
    """ViewSet для заказа"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["list"]:
            return [IsAdminUser()]
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []
