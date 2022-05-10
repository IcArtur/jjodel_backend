"""Define urls for jjodel app."""
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from jjodel.jjodel.viewsets.organization import OrganizationViewSet

urlpatterns = [
    path("token/", obtain_auth_token, name="obtain_auth_token"),

    path("", include("jjodel.jjodel.routers.organization")),
    path("", include("jjodel.jjodel.routers.model")),
    path("", include("jjodel.jjodel.routers.user")),

    path("organization/<Group>/", include("jjodel.jjodel.routers.member")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.admin")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.request")),

    path("user/<username>/", include("jjodel.jjodel.routers.viewpoint")),
    path("user/<username>/", include("jjodel.jjodel.routers.view")),

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

]
