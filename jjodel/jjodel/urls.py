"""Define urls for jjodel app."""
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("token/", obtain_auth_token, name="obtain_auth_token"),
    path("organization/<Group>/", include("jjodel.jjodel.routers.member")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.admin")),
    path("organization/<Group>/", include("jjodel.jjodel.routers.request")),
    # path("organization/", include("jjodel.jjodel.routers.request")),
]
