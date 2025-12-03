from rest_framework.routers import SimpleRouter

from core.viewsets import TelegramUserViewSet

router = SimpleRouter()

router.register(r'users', TelegramUserViewSet, basename='users')
