"""Viewpoint REST Api viewset."""
from jjodel.jjodel.models import AdminMember, GroupMember, Organization, User, Viewpoint
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.serializers.viewpoint import ViewpointSerializer


class ViewpointViewSet(viewsets.ModelViewSet):
    """Viewpoint ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewpointSerializer
    lookup_field = 'name'

    def get_queryset(self):
        """Define queryset for ViewpointViewSet class. This filters the users."""
        name = self.kwargs["name"]
        return Viewpoint.objects.filter(name=name)
