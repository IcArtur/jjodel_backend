"""Viewpoint REST Api viewset."""
from jjodel.jjodel.models import Viewpoint
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.permissions.viewpoint import ViewpointPermission
from jjodel.jjodel.serializers.viewpoint import ViewpointSerializer


class ViewpointViewSet(viewsets.ModelViewSet):
    """Viewpoint ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewpointSerializer
    permission_classes = [ViewpointPermission]
    lookup_field = 'name'

    def get_queryset(self):
        """Define queryset for ViewpointViewSet class. This filters organizations."""
        # I considered the bool value true when 1 is passed.
        if self.action == 'list':
            is_regexp = self.request.query_params.get('regex') == '1'
            vpname = self.request.query_params.get('vpname') or ''
            author = self.request.query_params.get('author') or ''
            if is_regexp:
                qs = Viewpoint.objects.filter(name__regex=rf'{vpname}',
                                              author__username__icontains=author)
            else:
                qs = Viewpoint.objects.filter(name__icontains=vpname,
                                              author__username__icontains=author)
        else:
            qs = Viewpoint.objects.filter(name__iexact=self.kwargs["name"])
        return qs

