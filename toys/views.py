from django.shortcuts import render
from django_filters import Filter
from rest_framework import generics
from rest_framework.views import APIView

from toys.models import Toy, Brend
from toys.serializer import ToySerializer, BrendSerializer


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


class BrendAPI(generics.ListCreateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class BrendAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
