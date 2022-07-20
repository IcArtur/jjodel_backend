"""Model router."""
from rest_framework.routers import DefaultRouter

from jjodel.model.viewsets import ModelViewSet

router = DefaultRouter()
router.register(r"model", ModelViewSet, basename="model_viewset")

urlpatterns = router.urls
