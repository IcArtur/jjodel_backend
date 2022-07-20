"""Admin REST Api viewset."""
from jjodel.jjodel.models import AdminMember, Organization, User
from jjodel.jjodel.serializers.user import UserSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class AdminMembersViewSet(viewsets.ModelViewSet):
    """AdminMembers ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer

    def get_queryset(self):
        """Define queryset for AdminMembersViewSet class. This filters the admin."""
        group_name = self.kwargs["Group"]
        return User.objects.filter(adminmember__organization__name=group_name)

    def update(self, request, *args, **kwargs):
        """Create new Admin for a group."""
        try:
            # Only admin and owner can make new admin
            # kwargs['pk'] is the username, it's not possible to change the lookup name
            user = User.objects.get(username=kwargs["pk"])
            organization = Organization.objects.get(name=kwargs["Group"])
            # Owners can add Admins
            is_owner = organization.owner == request.user
            is_admin = AdminMember.objects.filter(
                admin=request.user, organization=organization
            ).exists()
            if is_admin or is_owner:
                AdminMember.objects.update_or_create(
                    admin=user, organization=organization
                )
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """Remove Admin from a group."""
        try:
            # Only owner can remove admins.
            user = User.objects.get(username=kwargs["pk"])
            organization = Organization.objects.get(name=kwargs["Group"])
            is_owner = organization.owner == request.user
            if is_owner:
                AdminMember.objects.get(admin=user, organization=organization).delete()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

