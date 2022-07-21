"""ViewpointUserVisibility REST Api viewset."""
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.organization.permissions import ShareVisibilityPermission
from jjodel.user.models import User
from jjodel.user.serializers.user_visibility.user_viewpoint import \
    ViewpointUserVisibilitySerializer
from jjodel.viewpoint.models import ViewpointUserVisibility, Viewpoint


class ViewpointUserVisibilityViewSet(viewsets.ModelViewSet):
    """ViewpointUserVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewpointUserVisibilitySerializer
    permission_classes = [ShareVisibilityPermission]
    lookup_field = "user__username"

    def get_queryset(self):
        """Define queryset for ViewpointUserVisibility class."""
        author = self.kwargs["username"]
        vpname = self.kwargs["vpname"]
        return ViewpointUserVisibility.objects.filter(
            viewpoint__name=vpname, viewpoint__author__username=author
        )

    def update(self, request, *args, **kwargs):
        """PUT method, create or update."""
        try:
            user = User.objects.get(username=kwargs["user__username"])
            vp = Viewpoint.objects.get(name=kwargs["vpname"])
            readonly = request.query_params.get("readonly") == "1"
            ViewpointUserVisibility.objects.update_or_create(user=user, viewpoint=vp)
            ViewpointUserVisibility.objects.filter(user=user, viewpoint=vp).update(
                readonly=readonly
            )
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
