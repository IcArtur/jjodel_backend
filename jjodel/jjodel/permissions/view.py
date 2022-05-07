"""View file of permission package."""
from django.db.models import Q

from jjodel.jjodel.models import Organization, Viewpoint, ViewOrgVisibility, \
    ViewUserVisibility, View
from rest_framework import permissions

from jjodel.jjodel.models.viewpoint import ViewpointOrgVisibility


class ViewPermission(permissions.BasePermission):
    """Check view viewset permission."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and membership."""
        if view.action == 'list':
            return True
        if view.action == 'update':
            return view.kwargs['username'] == request.user.username
        if view.action == 'partial_update':
            viewname = view.kwargs["name"]
            view_object = View.objects.get(name__iexact=viewname)
            # First filter organizations in which the user is in
            orgs = Organization.objects.filter(
                Q(groupmember__member=request.user) | Q(
                    adminmember__admin=request.user) | Q(owner=request.user))
            # Then check if those orgs has visibility access on viewpoint
            orgs_share = ViewOrgVisibility.objects.filter(view=view_object,
                                                          organization__in=orgs,
                                                          readonly=False).exists()
            user_share = ViewUserVisibility.objects.filter(view=view_object,
                                                           user=request.user,
                                                           readonly=False).exists()
            if not view_object.is_public:
                # If view is not public it can be seen by author or shared.
                return request.user == view_object.author or orgs_share or user_share
        return True

    def has_object_permission(self, request, view, obj):
        """Detail permission check."""
        if view.action == 'destroy':
            # Only if the request user is the author the view can be deleted.
            return request.user == obj.author
        if not obj.is_public:
            orgs = Organization.objects.filter(
                Q(groupmember__member=request.user) | Q(
                    adminmember__admin=request.user) | Q(owner=request.user))
            user_share = ViewUserVisibility.objects.filter(view=obj, user=request.user)
            orgs_share = ViewOrgVisibility.objects.filter(view=obj,
                                                          organization__in=orgs).exists()
            return orgs_share or user_share
        return True