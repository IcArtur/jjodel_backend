"""ModelViewpoint router."""
from rest_framework.routers import DefaultRouter

from jjodel.viewpoint.viewsets import ViewpointViewViewSet

router = DefaultRouter()
router.register(r"view", ViewpointViewViewSet,
                basename="viewpoint_view_viewset")

urlpatterns = router.urls
