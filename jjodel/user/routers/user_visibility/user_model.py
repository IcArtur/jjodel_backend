"""Modeluser router."""
from jjodel.user.viewsets.user_visibility.user_model import ModelUserVisibilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"user", ModelUserVisibilityViewSet, basename="modeluser_viewset")

urlpatterns = router.urls
