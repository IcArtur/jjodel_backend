"""ViewOrgVisibility REST Api viewset."""
from jjodel.jjodel.models import Organization, View, ViewOrgVisibility
from jjodel.jjodel.permissions.visibility.orguser_visibility import (
    ShareVisibilityPermission,
)
from jjodel.organization.serializers.org_visibility.org_view import (
    ViewOrgVisibilitySerializer,
)
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ViewOrgVisibilityViewSet(viewsets.ModelViewSet):
    """ViewOrgVisibilityViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewOrgVisibilitySerializer
    permission_classes = [ShareVisibilityPermission]
    lookup_field = "organization__name"

    def get_queryset(self):
        """Define queryset for ViewOrgVisibility class."""
        author = self.kwargs["username"]
        view = self.kwargs["viewname"]
        return ViewOrgVisibility.objects.filter(
            view__name=view, view__author__username=author
        )

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            organization = Organization.objects.get(name=kwargs["organization__name"])
            view = View.objects.get(name=kwargs["viewname"])
            readonly = request.query_params.get("readonly") == "1"
            ViewOrgVisibility.objects.update_or_create(
                organization=organization, view=view
            )
            ViewOrgVisibility.objects.filter(
                organization=organization, view=view
            ).update(readonly=readonly)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
