"""MembershipRequest REST Api viewset."""
from jjodel.jjodel.models import AdminMember, Organization, User, MembershipRequest, \
    GroupMember
from jjodel.jjodel.serializers.user import UserSerializer, MembershipRequestSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class MembershipRequestViewSet(viewsets.ModelViewSet):
    """MembershipRequestViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    # permission_classes = [RequestPermission]
    serializer_class = MembershipRequestSerializer

    def list(self, request, *args, **kwargs):
        """Permission check for list method."""
        try:
            if self.check_admin_permission(request, kwargs["Group"]):
                return super().list(self, request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        """Permission check for retrieve method."""
        try:
            is_requester = MembershipRequest.objects.filter(
                member_id=kwargs["pk"]).exists()
            if self.check_admin_permission(request, kwargs["Group"]) and is_requester:
                return super().retrieve(self, request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        """Add Member to group."""
        try:
            user = User.objects.get(username=kwargs["pk"])
            organization = Organization.objects.get(name=kwargs["Group"])
            # Only the user can make a Request for himself.
            if user == request.user:
                # If org has open membership we put the user directly in it.
                if organization.openMembership:
                    GroupMember.objects.update_or_create(
                        member=user, organization_fk=organization
                    )
                    # If open membership we return 200 OK.
                    return Response(status=status.HTTP_200_OK)
                else:
                    # Add a request for the user
                    MembershipRequest.objects.update_or_create(
                        organization=organization,
                        member=user)
            else:
                # Only the user can request membership.
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """Remove request from group requests."""
        try:
            user = User.objects.get(username=kwargs["pk"])
            organization = Organization.objects.get(name=kwargs["Group"])
            # MembershipRequest user, admin and owner can cancel requests.
            if request.user == user or self.check_admin_permission(request,
                                                                   kwargs["Group"]):
                MembershipRequest.objects.get(
                    member=user, organization=organization
                ).delete()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

    def get_serializer_class(self):
        """Get different serializer based on different actions."""
        # if self.action == 'list':
        #     return MembershipRequestSerializer
        if self.action == 'retrieve':
            return UserSerializer
        return MembershipRequestSerializer

    def get_queryset(self):
        """Define queryset for AdminMembersViewSet class. This filters the admin."""
        if self.action == 'retrieve':
            return User.objects.filter()
        group_name = self.kwargs["Group"]
        return MembershipRequest.objects.filter(organization__name=group_name)

    @staticmethod
    def check_admin_permission(request, group):
        """Check admin permission."""
        organization = Organization.objects.get(name=group)
        # Owners can add Admins
        is_owner = organization.owner == request.user
        is_admin = AdminMember.objects.filter(
            admin=request.user, organization=organization
        ).exists()
        return is_admin or is_owner
