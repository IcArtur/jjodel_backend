"""Viewpoint router."""
from jjodel.jjodel.viewsets.viewpoint import ViewpointViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"viewpoint", ViewpointViewSet, basename="viewpoint_viewset")

urlpatterns = router.urls
