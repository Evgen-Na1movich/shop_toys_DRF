import pytest
from rest_framework.reverse import reverse

from rest_framework.status import HTTP_200_OK


@pytest.mark.django_db
def test_get_list_toys(api_client):
    """Тест успешного получения всех товаров"""
    url = 'http://127.0.0.1:8000/toys/'
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_get_list_toys_price(api_client):
    """Тест получения всех товаров с ценной меньше или равно 30"""
    url = 'http://localhost:8000/toys/?price_to=30'
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_get_list_toys_by_brend(api_client):
    """Тест получения всех товаров по бренду"""
    url = 'http://localhost:8000/brend/?brend=Lego'
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_get_product(api_client, product_factory):
    """Проверка получения 1го товара"""
    product = product_factory()
    url = reverse('products-detail', args=(product.id,))
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK
    response_json = responce.json()
    assert response_json['id'] == product.id
