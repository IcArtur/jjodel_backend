"""View router."""
from rest_framework.routers import DefaultRouter

from jjodel.view.viewsets import ViewRequirementViewSet

router = DefaultRouter()
router.register(r"requirement", ViewRequirementViewSet, basename="viewrequirement_viewset")

urlpatterns = router.urls
