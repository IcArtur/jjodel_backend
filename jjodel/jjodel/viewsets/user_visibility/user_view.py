"""ViewUserVisibility REST Api viewset."""
from jjodel.jjodel.models import User, View, Viewpoint, ViewUserVisibility
from jjodel.jjodel.permissions.visibility.orguser_visibility import (
    ShareVisibilityPermission,
)
from jjodel.jjodel.serializers.user_visibility.user_view import (
    ViewUserVisibilitySerializer,
)
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ViewUserVisibilityViewSet(viewsets.ModelViewSet):
    """ViewUserVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewUserVisibilitySerializer
    permission_classes = [ShareVisibilityPermission]
    lookup_field = "user__username"

    def get_queryset(self):
        """Define queryset for ViewViewSet class. This filters View."""
        author = self.kwargs["username"]
        view = self.kwargs["viewname"]
        return ViewUserVisibility.objects.filter(
            view__name=view, view__author__username=author
        )

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            user = User.objects.get(username=kwargs["user__username"])
            view = View.objects.get(name=kwargs["viewname"])
            readonly = request.query_params.get("readonly") == "1"
            ViewUserVisibility.objects.update_or_create(user=user, view=view)
            ViewUserVisibility.objects.filter(user=user, view=view).update(
                readonly=readonly
            )
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
