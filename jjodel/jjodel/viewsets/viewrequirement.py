"""ViewUserVisibility REST Api viewset."""
from jjodel.jjodel.models import User, View, Viewpoint, ViewUserVisibility, \
    ViewRequirement
from jjodel.jjodel.permissions.visibility.orguser_visibility import (
    ShareVisibilityPermission,
)
from jjodel.jjodel.serializers.user_visibility.user_view import (
    ViewUserVisibilitySerializer,
)
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.serializers.view_requirement import ViewRequirementSerializer


class ViewRequirementViewSet(viewsets.ModelViewSet):
    """ViewUserVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewRequirementSerializer
    permission_classes = [ShareVisibilityPermission]

    def get_queryset(self):
        """Define queryset for ViewViewSet class. This filters View."""
        author = self.kwargs["username"]
        view = self.kwargs["viewname"]
        return ViewRequirement.objects.filter(
            view__name=view, view__author__username=author
        )

    def create(self, request, *args, **kwargs):
        """POST method, create."""
        try:
            d = self.get_data_dict(request.data)
            view = View.objects.get(name=kwargs["viewname"])
            ViewRequirement.objects.create(**d, view=view)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """PATCH method, update"""
        try:
            d = self.get_data_dict(request.data)
            ViewRequirement.objects.filter(pk=kwargs["pk"]).update(**d)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_data_dict(data):
        """Create dict from data"""
        d = {"oclString": data["oclString"]}
        if data.get("comment"):
            d["comment"] = data["comment"]
        return d
