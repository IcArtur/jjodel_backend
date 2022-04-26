"""Organization router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.views.organization import GroupMembersViewSet

router = DefaultRouter()
router.register(r'member', GroupMembersViewSet, basename='group_members_viewset')

urlpatterns = router.urls
