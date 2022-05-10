"""ModelViewpoint router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.model_viewpoint import ModelViewpointViewSet

router = DefaultRouter()
router.register(r"viewpoint", ModelViewpointViewSet,
                basename="model_viewpoint_viewset")

urlpatterns = router.urls
