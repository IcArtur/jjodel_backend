"""Admin router."""
from jjodel.user.viewsets.admin import AdminMembersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"admin", AdminMembersViewSet, basename="admin_members_viewset")

urlpatterns = router.urls
