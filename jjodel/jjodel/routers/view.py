"""View router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.view import ViewViewSet

router = DefaultRouter()
router.register(r"view", ViewViewSet, basename="view_viewset")

urlpatterns = router.urls
