"""Define urls for jjodel app."""
from django.urls import include, path

urlpatterns = [
    path("user/<username>/", include("jjodel.viewpoint.routers.viewpoint")),
    path("user/<username>/viewpoint/<vpname>/",
         include("jjodel.viewpoint.routers.viewpoint_view")),
]
