"""Define urls for user app."""
from django.urls import include, path

urlpatterns = [
    path("", include("jjodel.user.routers.user")),
    path("organization/<Group>/", include("jjodel.user.routers.member")),
    path("organization/<Group>/", include("jjodel.user.routers.admin")),
    path("organization/<Group>/", include("jjodel.user.routers.request")),
    # View Visibility
    path(
        "user/<username>/view/<viewname>/",
        include("jjodel.user.routers.user_visibility.user_view"),
    ),
    # Viewpoint Visibility
    path(
        "user/<username>/viewpoint/<vpname>/",
        include("jjodel.user.routers.user_visibility.user_viewpoint"),
    ),
    # Model Visibility
    path(
        "user/<username>/model/<namespace>/",
        include("jjodel.user.routers.user_visibility.user_model"),
    ),
]
