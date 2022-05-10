"""Model router."""
from jjodel.jjodel.viewsets.model import ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"model", ModelViewSet, basename="model_viewset")

urlpatterns = router.urls
