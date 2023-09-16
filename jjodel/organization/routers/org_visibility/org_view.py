"""Vieworg router."""
from jjodel.organization.viewsets.org_visibility.org_view import (
    ViewOrgVisibilityViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"org", ViewOrgVisibilityViewSet, basename="vieworg_viewset")

urlpatterns = router.urls
