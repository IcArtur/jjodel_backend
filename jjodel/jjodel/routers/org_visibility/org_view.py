"""Vieworg router."""
from jjodel.jjodel.viewsets.org_visibility.org_view import ViewOrgVisibilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"org", ViewOrgVisibilityViewSet, basename="vieworg_viewset")

urlpatterns = router.urls
