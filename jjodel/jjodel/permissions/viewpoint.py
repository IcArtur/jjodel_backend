"""Viewpoint file of permission package."""
from django.db.models import Q

from jjodel.jjodel.models import AdminMember, GroupMember, Organization, Viewpoint
from rest_framework import permissions

from jjodel.jjodel.models.viewpoint import ViewpointOrgVisibility


class ViewpointPermission(permissions.BasePermission):
    """Check viewpoint viewset permission."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and membership."""
        if view.action == 'retrieve':
            vpname = view.kwargs["name"]
            vp = Viewpoint.objects.get(name__iexact=vpname)
            # First filter organizations in which the user is in
            orgs = Organization.objects.filter(
                Q(groupmember__member=request.user) | Q(
                    adminmember__admin=request.user) | Q(owner=request.user))
            # Then check if those orgs has visibility access on viewpoint
            orgs_visibility = ViewpointOrgVisibility.objects.filter(viewpoint=vp,
                                                                    organization__in=orgs).exists()
            if not vp.is_public:
                # If viewpoint is not public it can be seen by author or shared groups.
                return request.user == vp.author or orgs_visibility
        return True

    # def has_object_permission(self, request, view, obj):
    #     """Detail permission check."""
    #     vpname = view.kwargs["name"]
    #     vp = Viewpoint.objects.get(name=vpname)
    #     if not vp.is_public:
    #         # If viewpoint is not public only the author can see it.
    #         return request.user == vp.author
    #     else:
    #         return True


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
