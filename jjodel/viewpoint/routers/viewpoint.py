"""Viewpoint router."""
from jjodel.viewpoint.viewsets import ViewpointViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r"viewpoint", ViewpointViewSet, basename="viewpoint_viewset")

urlpatterns = router.urls
