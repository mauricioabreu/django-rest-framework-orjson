import pytest
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Game

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


def test_detail(client):
    url = reverse('game-detail', args=[1])
    data = {
        'name': 'The Legend of Zelda: Ocarina of Time',
    }
    Game.objects.create(**data)
    response = client.get(url, format='json')
    json = response.json()
    assert json['name'] == 'The Legend of Zelda: Ocarina of Time'


def test_list(client):
    url = reverse('game-list')
    data = {
        'name': 'The Legend of Zelda: Ocarina of Time',
    }
    Game.objects.create(**data)
    response = client.get(url, format='json')
    json = response.json()
    assert json[0]['name'] == 'The Legend of Zelda: Ocarina of Time'


def test_create(api_client):
    url = reverse('game-list')
    data = {
        'name': 'The Legend of Zelda: Ocarina of Time',
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
