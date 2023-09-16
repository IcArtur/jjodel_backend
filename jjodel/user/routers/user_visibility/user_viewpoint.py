"""Viewpointuser router."""
from jjodel.user.viewsets.user_visibility.user_viewpoint import (
    ViewpointUserVisibilityViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(
    r"user", ViewpointUserVisibilityViewSet, basename="viewpointuser_viewset"
)

urlpatterns = router.urls
