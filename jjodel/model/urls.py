"""Define urls for jjodel app."""
from django.urls import include, path

urlpatterns = [
    path("model/<namespace>/", include("jjodel.model.routers.model_viewpoint")),
]
