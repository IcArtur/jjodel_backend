"""Admin router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.admin import AdminMembersViewSet

router = DefaultRouter()
router.register(r'admin', AdminMembersViewSet, basename='admin_members_viewset')

urlpatterns = router.urls
