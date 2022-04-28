"""Viewpoint router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.viewpoint import ViewpointViewSet

router = DefaultRouter()
router.register(r"viewpoint", ViewpointViewSet, basename="viewpoint_viewset")

urlpatterns = router.urls
