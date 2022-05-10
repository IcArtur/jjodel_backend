"""Organization router."""
from jjodel.jjodel.viewsets.member import GroupMembersViewSet
from jjodel.jjodel.viewsets.organization import OrganizationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("organization", OrganizationViewSet, basename="organization_viewset")

urlpatterns = router.urls
