"""Define urls for jjodel app."""
from django.urls import include, path

urlpatterns = [
    path("", include("jjodel.model.routers.model")),
    path("model/<namespace>/", include("jjodel.model.routers.model_viewpoint")),
]
