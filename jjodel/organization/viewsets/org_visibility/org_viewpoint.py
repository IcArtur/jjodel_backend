"""ViewpointOrgVisibility REST Api viewset."""
from jjodel.organization.models import Organization
from jjodel.organization.permissions import ShareVisibilityPermission
from jjodel.organization.serializers.org_visibility.org_viewpoint import (
    ViewpointOrgVisibilitySerializer,
)
from jjodel.viewpoint.models import Viewpoint, ViewpointOrgVisibility
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ViewpointOrgVisibilityViewSet(viewsets.ModelViewSet):
    """ViewpointOrgVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewpointOrgVisibilitySerializer
    permission_classes = [ShareVisibilityPermission]
    lookup_field = "organization__name"

    def get_queryset(self):
        """Define queryset for ViewpointOrgVisibility class."""
        author = self.kwargs["username"]
        vpname = self.kwargs["vpname"]
        return ViewpointOrgVisibility.objects.filter(
            viewpoint__name=vpname, viewpoint__author__username=author
        )

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            organization = Organization.objects.get(name=kwargs["organization__name"])
            vp = Viewpoint.objects.get(name=kwargs["vpname"])
            readonly = request.query_params.get("readonly") == "1"
            ViewpointOrgVisibility.objects.update_or_create(
                organization=organization, viewpoint=vp
            )
            ViewpointOrgVisibility.objects.filter(
                organization=organization, viewpoint=vp
            ).update(readonly=readonly)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
