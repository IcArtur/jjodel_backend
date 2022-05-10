"""Viewuser router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.user_visibility.user_view import ViewUserVisibilityViewSet

router = DefaultRouter()
router.register(r"user", ViewUserVisibilityViewSet, basename="viewuser_viewset")

urlpatterns = router.urls
