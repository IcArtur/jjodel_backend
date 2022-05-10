"""Modeluser router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.user_visibility.user_model import ModelUserVisibilityViewSet

router = DefaultRouter()
router.register(r"user", ModelUserVisibilityViewSet,
                basename="modeluser_viewset")

urlpatterns = router.urls
