"""Organization router."""
from jjodel.organization.viewsets.viewsets import OrganizationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register("organization", OrganizationViewSet, basename="organization_viewset")

urlpatterns = router.urls
