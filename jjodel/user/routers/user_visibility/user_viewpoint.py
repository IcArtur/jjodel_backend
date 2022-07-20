"""Viewpointuser router."""
from jjodel.user.viewsets.user_visibility import (
    ViewpointUserVisibilityViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r"user", ViewpointUserVisibilityViewSet, basename="viewpointuser_viewset"
)

urlpatterns = router.urls
