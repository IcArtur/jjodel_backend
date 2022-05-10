"""Define urls for jjodel app."""
from django.urls import include, path
from jjodel.jjodel.viewsets.organization import OrganizationViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("token/", obtain_auth_token, name="obtain_auth_token"),
    path("", include("jjodel.jjodel.routers.organization")),
    path("", include("jjodel.jjodel.routers.model")),
    path("", include("jjodel.jjodel.routers.user")),
    path("model/<namespace>/", include("jjodel.jjodel.routers.model_viewpoint")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.member")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.admin")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.request")),
    path("user/<username>/", include("jjodel.jjodel.routers.viewpoint")),
    path("user/<username>/", include("jjodel.jjodel.routers.view")),
    path("user/<username>/viewpoint/<vpname>/",
         include("jjodel.jjodel.routers.viewpoint_view")),
    # View Visibility
    path("user/<username>/view/<viewname>/",
         include("jjodel.jjodel.routers.user_visibility.user_view")),
    path("user/<username>/view/<viewname>/",
         include("jjodel.jjodel.routers.org_visibility.org_view")),
    # Viewpoint Visibility
    path("user/<username>/viewpoint/<vpname>/",
         include("jjodel.jjodel.routers.user_visibility.user_viewpoint")),
    path("user/<username>/viewpoint/<vpname>/",
         include("jjodel.jjodel.routers.org_visibility.org_viewpoint")),
    # Model Visibility
    path("user/<username>/model/<namespace>/",
         include("jjodel.jjodel.routers.user_visibility.user_model")),
    path("user/<username>/model/<namespace>/",
         include("jjodel.jjodel.routers.org_visibility.org_model")),
    # Viewrequirement
    path("user/<username>/view/<viewname>/",
         include("jjodel.jjodel.routers.viewrequirement"))
]
