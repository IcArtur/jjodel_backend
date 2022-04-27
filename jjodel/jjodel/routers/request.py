"""Request router."""
from jjodel.jjodel.viewsets.member import GroupMembersViewSet
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.request import MembershipRequestViewSet

router = DefaultRouter()
router.register(r"request", MembershipRequestViewSet, basename="request_viewset")

urlpatterns = router.urls
