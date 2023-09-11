from django.urls import path

from toys.views import APIToys, APIToysInfo, BrendAPI

urlpatterns = [

    path('', APIToys.as_view(), name='toys'),
    path('<int:pk>/', APIToysInfo.as_view()),
    path('brend/', BrendAPI.as_view(), name='brends'),

]
