from django.urls import path

from toys.views import ToysListAPIView, APIToysInfo, BrendAPI, CategoryListAPI, ToysByCategoryAPIView

urlpatterns = [

    path('', CategoryListAPI.as_view(), name='cats'),
    path('toys/', ToysListAPIView.as_view(), name='toys'),

    path('toys/<int:pk>/', APIToysInfo.as_view()),
    path('brend/', BrendAPI.as_view(), name='brends'),
    path('brend/', BrendAPI.as_view(), name='brends'),


    path('<int:pk>/', ToysByCategoryAPIView.as_view(), name='cats'),
]
