"""Member REST Api viewset."""
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.organization.models import Organization
from jjodel.user.models import User, AdminMember, GroupMember
from jjodel.user.permissions import IsGroupMember
from jjodel.user.serializers.serializers import UserSerializer


class GroupMembersViewSet(viewsets.ModelViewSet):
    """GroupMembers ViewSet."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsGroupMember]
    serializer_class = UserSerializer

    def get_queryset(self):
        """Define queryset for GroupMembersViewSet class. This filters the users."""
        group_name = self.kwargs["Group"]
        return User.objects.filter(groupmember__organization_fk__name=group_name)

    def update(self, request, *args, **kwargs):
        """Add Member to group."""
        try:
            user = User.objects.get(username=kwargs["pk"])
            organization = Organization.objects.get(name=kwargs["Group"])
            is_owner = organization.owner == request.user
            is_admin = AdminMember.objects.filter(
                admin=request.user, organization=organization
            ).exists()
            # If org is open, user is admin or user is owner.
            if organization.openMembership or is_admin or is_owner:
                GroupMember.objects.update_or_create(
                    member=user, organization_fk=organization
                )
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """Remove member from group."""
        try:
            user = User.objects.get(username=kwargs["pk"])
            organization = Organization.objects.get(name=kwargs["Group"])
            is_owner = organization.owner == request.user
            is_admin = AdminMember.objects.filter(
                admin=request.user, organization=organization
            ).exists()
            # User can exit, admin and owner can remove users.
            if request.user == user or is_admin or is_owner:
                GroupMember.objects.get(
                    member=user, organization_fk=organization
                ).delete()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)
