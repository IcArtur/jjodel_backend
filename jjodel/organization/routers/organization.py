"""Organization router."""
from rest_framework.routers import DefaultRouter

from jjodel.organization.viewsets.viewsets import OrganizationViewSet

router = DefaultRouter()
router.register("organization", OrganizationViewSet, basename="organization_viewset")

urlpatterns = router.urls
