from django.urls import path, include
from toys.views import ToyViewSet, CategoryViewSet, BrendViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('toys', ToyViewSet) # toys - URL, который будет использоваться для этого набора маршрутов
router.register('cats', CategoryViewSet)
router.register('brend', BrendViewSet)

print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]
