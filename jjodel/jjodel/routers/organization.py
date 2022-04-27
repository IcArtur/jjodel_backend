"""Organization router."""
from jjodel.jjodel.viewsets.member import GroupMembersViewSet
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.organization import OrganizationViewSet

router = DefaultRouter()
router.register("organization", OrganizationViewSet, basename="organization_viewset")

urlpatterns = router.urls
