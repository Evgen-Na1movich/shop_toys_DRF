from django.shortcuts import render
from django_filters import Filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from toys.models import Toy, Brend, Category
from toys.serializer import ToySerializer, BrendSerializer, CategorySerializer


class CategoryListAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ToysListAPIView(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filter_backends = [SearchFilter]
    search_fields = ('categories', 'brend')


class APIToysInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class BrendAPI(generics.ListCreateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class BrendListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class ToysByCategoryAPIView(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_filds = ['categories' ]
