"""Request router."""
from jjodel.user.viewsets.request import MembershipRequestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"request", MembershipRequestViewSet, basename="request_viewset")

urlpatterns = router.urls
