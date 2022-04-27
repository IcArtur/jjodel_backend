"""Member router."""
from jjodel.jjodel.viewsets.member import GroupMembersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"member", GroupMembersViewSet, basename="group_members_viewset")

urlpatterns = router.urls
