import uuid
import pytest

from django.conf import settings
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


# @pytest.fixture
# def product_factory():
#     def factory(**kwargs):
#         return baker.make('Item', **kwargs)
#
#     return factory
#
#
# @pytest.fixture
# def user_factory():
#     def factory(**kwargs):
#         return baker.make(settings.AUTH_USER_MODEL)
#
#     return factory
#
#
# @pytest.fixture
# def order_factory():
#     def factory(**kwargs):
#         return baker.make('Order', **kwargs)
#
#     return factory
