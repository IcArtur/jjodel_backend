"""Organization router."""
from jjodel.organization.viewsets.viewsets import OrganizationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("organization", OrganizationViewSet, basename="organization_viewset")

urlpatterns = router.urls
