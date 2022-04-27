"""Admin router."""
from jjodel.jjodel.viewsets.admin import AdminMembersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"admin", AdminMembersViewSet, basename="admin_members_viewset")

urlpatterns = router.urls
