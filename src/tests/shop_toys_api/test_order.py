import pytest
from rest_framework.status import HTTP_201_CREATED


@pytest.mark.django_db
def test_create_order(api_client, product_factory, user_factory):
    """Проверка создания заказа авторизованным пользователем"""
    url = 'http://localhost:8000/orders/'
    user = user_factory()
    product = product_factory()
    data = {
        "positions": [
            {
                "product": product.id,
                "quantity": 4
            },
            {
                "product": product.id,
                "quantity": 3
            }
        ],
        "adress": "Тисовая улица, 4"
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == HTTP_201_CREATED