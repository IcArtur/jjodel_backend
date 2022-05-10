"""ModelViewpoint REST Api viewset."""
from jjodel.jjodel.models import Viewpoint, ModelViewpoint, Model
from jjodel.jjodel.permissions.visibility.orguser_visibility import (
    ShareVisibilityPermission,
)
from jjodel.jjodel.serializers.model_viewpoint import ModelViewpointSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ModelViewpointViewSet(viewsets.ModelViewSet):
    """ModelViewpoint ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ModelViewpointSerializer
    # permission_classes = [ShareVisibilityPermission]
    lookup_field = 'viewpoint__name'

    def get_queryset(self):
        """Define queryset for ModelViewpointViewSet class. This filters
        ModelViewpoint. """
        namespace = self.kwargs["namespace"]
        return ModelViewpoint.objects.filter(model__namespace=namespace)

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            model = Model.objects.get(namespace=kwargs["namespace"])
            vp = Viewpoint.objects.get(name=kwargs["viewpoint__name"])
            ModelViewpoint.objects.update_or_create(model=model, viewpoint=vp)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
