"""Member router."""
from jjodel.user.viewsets.member import GroupMembersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"member", GroupMembersViewSet, basename="group_members_viewset")

urlpatterns = router.urls
