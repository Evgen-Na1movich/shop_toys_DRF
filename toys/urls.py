from django.urls import path, include, re_path
from toys.views import ToyViewSet, CategoryViewSet, BrendViewSet, OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('toys', ToyViewSet) # toys - URL, который будет использоваться для этого набора маршрутов
router.register('cats', CategoryViewSet)
router.register('brend', BrendViewSet)
router.register('oder', OrderViewSet)

print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth-token/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),

]
