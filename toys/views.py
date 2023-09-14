from django.shortcuts import render
from django_filters import Filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from toys.filters import ToysFilter
from toys.models import Toy, Brend, Category
from toys.serializer import ToySerializer, BrendSerializer, CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories', ]


# class ToysListAPIView(generics.ListCreateAPIView):
#     queryset = Toy.objects.all()
#     serializer_class = ToySerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['categories', ]
#
#
# class ToyDetaislapiview(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Toy.objects.all()
#     serializer_class = ToySerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['categories', ]

class ToyViewSet(ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

    # filter_class = ToysFilter
    # filter_backends = [DjangoFilterBackend]

    @action(methods=["GET"], detail=True)
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

    def brend(self, request, pk):
        brend = Brend.objects.get(pk=pk)
        return Response({'brend': brend.name})


class BrendListAPIView(generics.ListCreateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class ToysByCategoryFilterAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filter_class = ToysFilter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories', ]


class BrendListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class ToysByCategoryAPIView(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_filds = ['categories']
