"""Model org router."""
from jjodel.organization.viewsets.org_visibility import ModelOrgVisibilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"org", ModelOrgVisibilityViewSet, basename="modelorg_viewset")

urlpatterns = router.urls
