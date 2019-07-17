from rest_framework.viewsets import ModelViewSet

from .models import Game
from .serializers import GameSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
