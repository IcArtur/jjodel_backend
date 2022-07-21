"""Model org router."""
from rest_framework.routers import DefaultRouter

from jjodel.organization.viewsets.org_visibility.org_model import \
    ModelOrgVisibilityViewSet

router = DefaultRouter()
router.register(r"org", ModelOrgVisibilityViewSet, basename="modelorg_viewset")

urlpatterns = router.urls
