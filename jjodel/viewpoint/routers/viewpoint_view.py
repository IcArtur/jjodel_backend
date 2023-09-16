"""ModelViewpoint router."""
from jjodel.viewpoint.viewsets import ViewpointViewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"view", ViewpointViewViewSet, basename="viewpoint_view_viewset")

urlpatterns = router.urls
