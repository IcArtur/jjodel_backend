"""Organization REST Api viewset."""
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.organization.models import Organization
from jjodel.organization.serializers.serializers import OrganizationSerializer
from jjodel.user.models import User, AdminMember, GroupMember


class OrganizationViewSet(viewsets.ModelViewSet):
    """OrganizationViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = OrganizationSerializer
    lookup_field = "name"

    def update(self, request, *args, **kwargs):
        """PUT method for organization."""
        # If the user already has created 10 orgs.
        if Organization.objects.filter(owner=request.user).count() >= 10:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            # Check if the name of the orgs is already taken
            if Organization.objects.filter(name=request.data["name"]).exists():
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={"message": "Organization already exists"},
                )
            d = self.get_data_dict(request.data)
            # Create new organization.
            Organization.objects.create(**d, owner=request.user)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        """PATCH method for organization."""
        try:
            # Check if the name of the orgs is already taken
            organization = Organization.objects.filter(name=kwargs["name"])
            d = self.get_data_dict(request.data)
            owner = User.objects.get(username=request.data["owner"])
            is_admin = AdminMember.objects.filter(
                organization=organization[0], admin=request.user
            ).exists()
            is_owner = request.user == organization[0].owner
            # Permission check
            if not is_admin and not is_owner:
                return Response(status=status.HTTP_403_FORBIDDEN)
            # Only the owner can change the owner
            if organization[0].owner != owner and request.user != organization[0].owner:
                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data={"message": "Admin can't change owner."},
                )
            # Update the organization.
            organization.update(**d, owner=owner)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """Delete organization."""
        try:
            organization = Organization.objects.filter(name=kwargs["name"])
            is_owner = organization[0].owner == request.user
            # Only owner can delete the organization.
            if is_owner:
                organization.delete()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """Permission check for GET detail method."""
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
        if self.action == "list":
            is_regexp = self.request.query_params["regexp"] == "1"
            name = self.request.query_params["name"]
            if is_regexp:
                qs = Organization.objects.filter(name__regex=rf"{name}")
            else:
                qs = Organization.objects.filter(name__icontains=name)
        else:
            qs = Organization.objects.filter()
        return qs

    @staticmethod
    def get_retrieve_permissions(request, groupname):
        """Permission for retrieve method."""
        organization = Organization.objects.get(name=groupname)
        is_member = GroupMember.objects.filter(
            organization_fk__name=groupname, member=request.user
        ).exists()
        is_owner = organization.owner == request.user
        is_admin = AdminMember.objects.filter(
            admin=request.user, organization=organization
        ).exists()
        # If the organization is not public user needs to be at least member.
        return organization.isPublic or is_member or is_owner or is_admin

    @staticmethod
    def get_data_dict(data):
        """Create dict from data"""
        d = {"name": data["name"]}
        if data.get("isPublic"):
            d["isPublic"] = data["isPublic"] == "1"
        if data.get("openMembership"):
            d["openMembership"] = data["openMembership"] == "1"
        if data.get("mail_domain_required"):
            d["mail_domain_required"] = data["mail_domain_required"]
        if data.get("bio"):
            d["bio"] = data["bio"]
        return d
