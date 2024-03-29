"""Model router."""
from jjodel.model.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"model", ModelViewSet, basename="model_viewset")

urlpatterns = router.urls
