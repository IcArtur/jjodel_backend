"""Viewpoint org router."""
from jjodel.organization.viewsets.org_visibility.org_viewpoint import (
    ViewpointOrgVisibilityViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"org", ViewpointOrgVisibilityViewSet, basename="viewpointorg_viewset")

urlpatterns = router.urls
