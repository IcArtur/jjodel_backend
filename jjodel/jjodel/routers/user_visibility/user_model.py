"""Modeluser router."""
from jjodel.jjodel.viewsets.user_visibility.user_model import ModelUserVisibilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", ModelUserVisibilityViewSet, basename="modeluser_viewset")

urlpatterns = router.urls
