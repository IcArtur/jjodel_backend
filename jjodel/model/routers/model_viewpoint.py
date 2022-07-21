"""ModelViewpoint router."""
from jjodel.model.viewsets import ModelViewpointViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"viewpoint", ModelViewpointViewSet, basename="model_viewpoint_viewset")

urlpatterns = router.urls
