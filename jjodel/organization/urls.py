"""Define urls for organization app."""
from django.urls import include, path

urlpatterns = [
    path("", include("jjodel.organization.routers.organization")),
    # View Visibility
    path(
        "user/<username>/view/<viewname>/",
        include("jjodel.organization.routers.org_visibility.org_view"),
    ),
    # Viewpoint Visibility
    path(
        "user/<username>/viewpoint/<vpname>/",
        include("jjodel.organization.routers.org_visibility.org_viewpoint"),
    ),
    # Model Visibility
    path(
        "user/<username>/model/<namespace>/",
        include("jjodel.organization.routers.org_visibility.org_model"),
    ),
]
