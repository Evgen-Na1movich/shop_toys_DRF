from django.shortcuts import render
from django_filters import Filter
from rest_framework import generics
from rest_framework.views import APIView

from toys.models import Toy
from toys.serializer import ToySerializer


class APIToys(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filterset_class = Filter

    # фильтрация по бренду
    def get_queryset(self):
        # получаем queryset, который есть и переопределяем его
        queryset = super(APIToys, self).get_queryset()
        queryset = queryset.filter(visible=True)
        return queryset


class APIToysInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
