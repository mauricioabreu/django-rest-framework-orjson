from rest_framework.serializers import ModelSerializer

from .models import Game


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "name",
        )
