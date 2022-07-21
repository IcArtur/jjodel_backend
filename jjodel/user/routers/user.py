"""User router."""
from jjodel.user.viewsets.user import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user_viewset")

urlpatterns = router.urls
