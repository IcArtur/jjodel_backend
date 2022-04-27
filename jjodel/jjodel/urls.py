"""Define urls for jjodel app."""
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from jjodel.jjodel.viewsets.organization import OrganizationViewSet

urlpatterns = [
    path("", include("jjodel.jjodel.routers.organization")),
    path("token/", obtain_auth_token, name="obtain_auth_token"),
    path("organization/<Group>/", include("jjodel.jjodel.routers.member")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.admin")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.request")),
]
