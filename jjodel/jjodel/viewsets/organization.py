"""Organization REST Api viewset."""
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.models import Organization, User, GroupMember, AdminMember
from jjodel.jjodel.serializers.organization import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """OrganizationViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = OrganizationSerializer
    lookup_field = 'name'

    # def list(self, request, *args, **kwargs):
    #     """Permission check for list method."""
    #     regexp = request.query_params["regexp"]
    #     name = request.query_params["name"]
    #     if regexp:
    #         pass
    #     return Response()

    def retrieve(self, request, *args, **kwargs):
        """Permission check for retrieve method."""
        try:
            if self.get_retrieve_permissions(request, kwargs["name"]):
                return super().retrieve(self, request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        """Define queryset for OrganizationViewSet class. This filters organizations."""
        # I considered the bool value true when 1 is passed.
        if self.action == 'list':
            is_regexp = self.request.query_params['regexp'] == '1'
            name = self.request.query_params['name']
            if is_regexp:
                qs = Organization.objects.filter(name__regex=rf'{name}')
            else:
                qs = Organization.objects.filter(name__icontains=name)
        else:
            qs = Organization.objects.filter()
        return qs

    @staticmethod
    def get_retrieve_permissions(request, groupname):
        """Permission for retrieve method."""
        organization = Organization.objects.get(name=groupname)
        is_member = GroupMember.objects.filter(organization_fk__name=groupname,
                                               member=request.user).exists()
        is_owner = organization.owner == request.user
        is_admin = AdminMember.objects.filter(
            admin=request.user, organization=organization
        ).exists()
        return organization.isPublic or is_member or is_owner or is_admin


    # def retrieve(self, request, *args, **kwargs):
    #     """Permission check for retrieve method."""
    #     pass
