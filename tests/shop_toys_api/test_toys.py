import pytest
from rest_framework.reverse import reverse

from rest_framework.status import HTTP_200_OK

from toys.models import Toy


@pytest.mark.django_db
def test_get_list_toys(api_client):
    """Тест успешного получения всех товаров"""
    url = 'http://127.0.0.1:8000/toys/'
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_get_toy(api_client, product_factory):
    """Тест успешного получения 1-й игрушки"""
    toy = product_factory()
    url = reverse('http://127.0.0.1:8000/toys/', args=(toy.id,))
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK
    responce_json = responce.json()
    assert responce_json['id'] == toy.id

