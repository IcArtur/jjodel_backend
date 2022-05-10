"""Model org router."""
from jjodel.jjodel.viewsets.org_visibility.org_model import ModelOrgVisibilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"org", ModelOrgVisibilityViewSet, basename="modelorg_viewset")

urlpatterns = router.urls
