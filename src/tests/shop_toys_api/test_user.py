import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED


@pytest.mark.django_db
def test_create_user(api_client):
    """Тест регистрации пользователя"""
    data = {
        "email": "potter@hogvards.com",
        "username": "Harry",
        "password": "ilovemagic"
    }
    url = 'http://localhost:8000/auth/users/'
    response = api_client.post(url, data)
    assert response.status_code == HTTP_201_CREATED
    user = User.objects.get(username="Harry")
    token = Token.objects.create(user=user)
    assert token.key
