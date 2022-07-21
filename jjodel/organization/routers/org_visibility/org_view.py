"""Vieworg router."""
from rest_framework.routers import DefaultRouter

from jjodel.organization.viewsets.org_visibility.org_view import \
    ViewOrgVisibilityViewSet

router = DefaultRouter()
router.register(r"org", ViewOrgVisibilityViewSet, basename="vieworg_viewset")

urlpatterns = router.urls
