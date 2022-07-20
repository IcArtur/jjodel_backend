"""Define urls for jjodel app."""
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("user/<username>/", include("jjodel.viewpoint.routers.viewpoint")),
    path("user/<username>/viewpoint/<vpname>/",
         include("jjodel.viewpoint.routers.viewpoint_view")),
]
