from rest_framework import routers

from .views import GameViewSet


app_name = 'game'
router = routers.SimpleRouter()
router.register('game', GameViewSet)
urlpatterns = router.urls
