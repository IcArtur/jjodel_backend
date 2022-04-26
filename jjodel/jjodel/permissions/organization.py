from rest_framework import permissions

from jjodel.jjodel.models import GroupMember


class IsGroupMember(permissions.BasePermission):
    """Check if request user is member of the group."""

    def has_permission(self, request, view):
        """First auth method, check user and authentication."""
        group_name = view.kwargs['Group']
        auth = request.user and request.user.is_authenticated
        GroupMember.objects.filter(organization_fk__name='Univaq')
        membership = GroupMember.objects.filter(organization_fk__name=group_name,
                                                member=request.user).exists()
        return auth and membership

    # def has_object_permission(self, request, view, obj):
    #     """Second auth method, check group membership."""
    #     # if request.method in permissions.SAFE_METHODS:
    #     #     return True
    #     check = GroupMember.objects.filter(organization_fk=obj,
    #                                        member=request.user).exists()
    #     return False
