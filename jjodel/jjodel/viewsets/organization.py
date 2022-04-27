"""Organization REST Api viewset."""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class OrganizationViewSet(viewsets.ModelViewSet):
    """OrganizationViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    # permission_classes = [RequestPermission]
    # serializer_class =


    def list(self, request, *args, **kwargs):
        """Permission check for list method."""
        pass

    def retrieve(self, request, *args, **kwargs):
        """Permission check for retrieve method."""
        pass

