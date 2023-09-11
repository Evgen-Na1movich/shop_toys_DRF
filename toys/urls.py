from django.urls import path

from toys.views import APIToys, APIToysInfo

urlpatterns = [

    path('', APIToys.as_view(), name='toys'),
    path('<int:pk>/', APIToysInfo.as_view()),
]
