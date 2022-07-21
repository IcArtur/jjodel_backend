"""Define urls for jjodel app."""
from django.urls import include, path

urlpatterns = [
    path("user/<username>/", include("jjodel.view.routers.view")),
    # Viewrequirement
    path(
        "user/<username>/view/<viewname>/",
        include("jjodel.view.routers.viewrequirement"),
    ),
]
