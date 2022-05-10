"""ViewpointView REST Api viewset."""
from jjodel.jjodel.models import Viewpoint, ModelViewpoint, Model, ViewpointView, View
from jjodel.jjodel.permissions.visibility.orguser_visibility import (
    ShareVisibilityPermission,
)
from jjodel.jjodel.serializers.model_viewpoint import ModelViewpointSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.serializers.viewpoint_view import ViewpointViewSerializer


class ViewpointViewViewSet(viewsets.ModelViewSet):
    """ViewpointView ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewpointViewSerializer
    # permission_classes = [ShareVisibilityPermission]
    lookup_field = 'view__name'

    def get_queryset(self):
        """Define queryset for ViewpointViewViewSet class. This filters
        ViewpointView. """
        return ViewpointView.objects.filter(viewpoint__name=self.kwargs["vpname"])

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            view = View.objects.get(name=kwargs["view__name"])
            vp = Viewpoint.objects.get(name=kwargs["vpname"])
            ViewpointView.objects.update_or_create(view=view, viewpoint=vp)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
