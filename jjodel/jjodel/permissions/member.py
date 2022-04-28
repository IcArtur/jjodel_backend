"""Member file of permission package."""
from jjodel.jjodel.models import AdminMember, GroupMember, Organization
from rest_framework import permissions


class IsGroupMember(permissions.BasePermission):
    """Check if request user is member of the group."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and membership."""
        try:
            group_name = view.kwargs["Group"]
            auth = request.user and request.user.is_authenticated
            is_member = GroupMember.objects.filter(
                organization_fk__name=group_name, member=request.user
            ).exists()
            is_admin = AdminMember.objects.filter(
                organization__name=group_name, admin=request.user
            ).exists()
            is_owner = Organization.objects.filter(owner=request.user).exists()
            return auth and (is_member or is_admin or is_owner)
        except Exception:
            return False


class IsAdminMember(permissions.BasePermission):
    """Check if request user is member of the group."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and adminship."""
        group_name = view.kwargs["Group"]
        auth = request.user and request.user.is_authenticated
        is_admin = AdminMember.objects.filter(
            organization__name=group_name, member=request.user
        ).exists()
        return auth and is_admin
