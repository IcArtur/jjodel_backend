"""ModelOrgVisibility REST Api viewset."""
from jjodel.jjodel.models import Organization
from jjodel.jjodel.models.model import Model, ModelOrgVisibility
from jjodel.jjodel.permissions.visibility.orguser_visibility import (
    ShareVisibilityPermission,
)
from jjodel.organization.serializers.org_visibility.org_model import (
    ModelOrgVisibilitySerializer,
)
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ModelOrgVisibilityViewSet(viewsets.ModelViewSet):
    """ModelOrgVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ModelOrgVisibilitySerializer
    permission_classes = [ShareVisibilityPermission]
    lookup_field = "organization__name"

    def get_queryset(self):
        """Define queryset for ModelOrgVisibility class."""
        author = self.kwargs["username"]
        model = self.kwargs["namespace"]
        return ModelOrgVisibility.objects.filter(
            model__namespace=model, model__author__username=author
        )

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            organization = Organization.objects.get(name=kwargs["organization__name"])
            model = Model.objects.get(namespace=kwargs["namespace"])
            readonly = request.query_params.get("readonly") == "1"
            ModelOrgVisibility.objects.update_or_create(
                organization=organization, model=model
            )
            ModelOrgVisibility.objects.filter(
                organization=organization, model=model
            ).update(readonly=readonly)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
