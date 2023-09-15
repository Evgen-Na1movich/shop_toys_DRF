from django.urls import path, include
from toys.views import ToyViewSet, CategoryViewSet, BrendViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('toys', ToyViewSet)
router.register('cats', CategoryViewSet)
router.register('brend', BrendViewSet)
# toys - URL, который будет использоваться для этого набора маршрутов
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]
