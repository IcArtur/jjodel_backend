"""View router."""
from jjodel.jjodel.viewsets.view import ViewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"view", ViewViewSet, basename="view_viewset")

urlpatterns = router.urls
