from django.urls import path, include
from toys.views import ToyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('toys', ToyViewSet)
# toys - URL, который будет использоваться для этого набора маршрутов
print(router.urls)

urlpatterns = [

    # path('', CategoryListAPIView.as_view(), name='cats'),
    # path('toys/', ToyViewSet.as_view(), name='toys'),
    # # path('toys/<int:pk>/', ToyDetaislapiview.as_view()),
    # path('brends/', BrendListAPIView.as_view(), name='brends'),
    # path('cats/<int:pk>/', CategoryDetailAPIView.as_view(), name='toys_by_category'),
    path('', include(router.urls)),
    # path('auth-drf/', include('rest_framework.urls')),

]
