"""Viewpoint file of permission package."""
from django.db.models import Q

from jjodel.jjodel.models import AdminMember, GroupMember, Organization, Viewpoint
from rest_framework import permissions

from jjodel.jjodel.models.viewpoint import ViewpointOrgVisibility, \
    ViewpointUserVisibility


class ViewpointPermission(permissions.BasePermission):
    """Check viewpoint viewset permission."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and membership."""
        if view.action == 'list':
            return True
        if view.action == 'update':
            return view.kwargs['username'] == request.user.username
        vpname = view.kwargs["name"]
        vp = Viewpoint.objects.get(name__iexact=vpname)
        # First filter organizations in which the user is in
        orgs = request.user.orgs
        # Then check if those orgs has visibility access on viewpoint
        vp_orgs = ViewpointOrgVisibility.objects.filter(viewpoint=vp,
                                                        organization__in=orgs)
        vp_user = ViewpointUserVisibility.objects.filter(viewpoint=vp,
                                                         user=request.user)
        visibility = vp_orgs.exists() or vp_user.exists()
        if view.action == 'partial_update':
            # Readonly condition
            not_readonly = vp_orgs.filter(readonly=False).exists() or vp_user.filter(
                readonly=False).exists()
            visibility = visibility and not_readonly
        if not vp.is_public:
            # If viewpoint is not public it can be seen by author or shared groups.
            return request.user == vp.author or visibility
        return True

    def has_object_permission(self, request, view, obj):
        """Detail permission check."""
        if view.action == "destroy":
            return request.user == obj.author
        else:
            return True
