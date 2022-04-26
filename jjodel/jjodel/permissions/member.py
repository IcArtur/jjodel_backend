from rest_framework import permissions

from jjodel.jjodel.models import GroupMember, AdminMember


class IsGroupMember(permissions.BasePermission):
    """Check if request user is member of the group."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and membership."""
        group_name = view.kwargs['Group']
        auth = request.user and request.user.is_authenticated
        membership = GroupMember.objects.filter(organization_fk__name=group_name,
                                                member=request.user).exists()
        return auth and membership


class IsAdminMember(permissions.BasePermission):
    """Check if request user is member of the group."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and adminship."""
        group_name = view.kwargs['Group']
        auth = request.user and request.user.is_authenticated
        adminship = AdminMember.objects.filter(organization__name=group_name,
                                                member=request.user).exists()
        return auth and adminship
