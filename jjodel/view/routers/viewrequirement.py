"""View router."""
from jjodel.view.viewsets import ViewRequirementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(
    r"requirement", ViewRequirementViewSet, basename="viewrequirement_viewset",
)

urlpatterns = router.urls
