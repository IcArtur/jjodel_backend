"""Request router."""
from jjodel.jjodel.viewsets.member import GroupMembersViewSet
from jjodel.jjodel.viewsets.request import MembershipRequestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"request", MembershipRequestViewSet, basename="request_viewset")

urlpatterns = router.urls
