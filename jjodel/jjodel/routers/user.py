"""User router."""
from jjodel.jjodel.viewsets.user import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user_viewset")

urlpatterns = router.urls
