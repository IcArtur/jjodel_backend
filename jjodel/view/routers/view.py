"""View router."""
from jjodel.view.viewsets import ViewViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r"view", ViewViewSet, basename="view_viewset")

urlpatterns = router.urls
