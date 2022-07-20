"""Viewuser router."""
from jjodel.user.viewsets.user_visibility.user_view import ViewUserVisibilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", ViewUserVisibilityViewSet, basename="viewuser_viewset")

urlpatterns = router.urls
