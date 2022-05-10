"""Viewpoint org router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.org_visibility.org_viewpoint import \
    ViewpointOrgVisibilityViewSet

router = DefaultRouter()
router.register(r"org", ViewpointOrgVisibilityViewSet, basename="viewpointorg_viewset")

urlpatterns = router.urls
