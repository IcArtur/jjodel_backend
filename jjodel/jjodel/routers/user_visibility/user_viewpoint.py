"""Viewpointuser router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.user_visibility.user_viewpoint import \
    ViewpointUserVisibilityViewSet

router = DefaultRouter()
router.register(r"user", ViewpointUserVisibilityViewSet,
                basename="viewpointuser_viewset")

urlpatterns = router.urls
