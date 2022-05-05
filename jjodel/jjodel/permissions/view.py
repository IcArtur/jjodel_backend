"""View file of permission package."""
from django.db.models import Q

from jjodel.jjodel.models import Organization, Viewpoint
from rest_framework import permissions

from jjodel.jjodel.models.viewpoint import ViewpointOrgVisibility


class ViewPermission(permissions.BasePermission):
    """Check view viewset permission."""

    # def has_permission(self, request, view):
    #     """Global auth method, check user, authentication and membership."""
    #     if view.action in ['list', 'update']:
    #         return True
    #     vpname = view.kwargs["name"]
    #     vp = Viewpoint.objects.get(name__iexact=vpname)
    #     # First filter organizations in which the user is in
    #     orgs = Organization.objects.filter(
    #         Q(groupmember__member=request.user) | Q(
    #             adminmember__admin=request.user) | Q(owner=request.user))
    #     # Then check if those orgs has visibility access on viewpoint
    #     orgs = ViewpointOrgVisibility.objects.filter(viewpoint=vp,
    #                                                  organization__in=orgs)
    #     orgs_visibility = orgs.exists()
    #     if view.action == 'partial_update':
    #         read_only = True
    #         for org in orgs:
    #             # If any of the ViewpointOrgVisibility has readonly=False read_only
    #             # will be false.
    #             read_only = read_only and org.readonly
    #             # Orgs visib will also be org read-only. If orgs_visibility will be
    #             # true the check will pass.
    #             orgs_visibility = orgs_visibility and not read_only
    #     if not vp.is_public:
    #         # If viewpoint is not public it can be seen by author or shared groups.
    #         return request.user == vp.author or orgs_visibility
    #     return True
    #
    # def has_object_permission(self, request, view, obj):
    #     """Detail permission check."""
    #     if view.action == "destroy":
    #         return request.user == obj.author
    #     else:
    #         return True
