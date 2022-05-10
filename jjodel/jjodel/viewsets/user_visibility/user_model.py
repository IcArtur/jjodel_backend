"""ModelUserVisibility REST Api viewset."""
from jjodel.jjodel.models import User
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.models.model import ModelUserVisibility, Model
from jjodel.jjodel.permissions.visibility.orguser_visibility import \
    ShareVisibilityPermission
from jjodel.jjodel.serializers.user_visibility.user_model import \
    ModelUserVisibilitySerializer


class ModelUserVisibilityViewSet(viewsets.ModelViewSet):
    """ModelUserVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ModelUserVisibilitySerializer
    permission_classes = [ShareVisibilityPermission]
    lookup_field = 'user__username'

    def get_queryset(self):
        """Define queryset for ModelUserVisibility class. """
        author = self.kwargs['username']
        model = self.kwargs['namespace']
        return ModelUserVisibility.objects.filter(model__namespace=model,
                                                  model__author__username=author)

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            user = User.objects.get(username=kwargs['user__username'])
            model = Model.objects.get(namespace=kwargs['namespace'])
            readonly = request.query_params.get('readonly') == '1'
            ModelUserVisibility.objects.update_or_create(user=user,
                                                         model=model)
            ModelUserVisibility.objects.filter(user=user,
                                               model=model).update(readonly=readonly)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
