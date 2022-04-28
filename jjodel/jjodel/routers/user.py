"""User router."""
from rest_framework.routers import DefaultRouter

from jjodel.jjodel.viewsets.user import UserViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user_viewset")

urlpatterns = router.urls
