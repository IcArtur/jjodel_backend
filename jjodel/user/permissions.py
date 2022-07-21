"""Member file of permission package."""
from rest_framework import permissions

from jjodel.organization.models import Organization
from jjodel.user.models import GroupMember, AdminMember


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


class RequestPermission(permissions.BasePermission):
    """Request ViewSet permission class."""

    def __init__(self):
        """Init method of RequestPermission class."""
        self.is_auth = False
        self.is_admin = False
        self.group_name = ""

    def has_permission(self, request, view):
        """Global permission method."""
        self.group_name = view.kwargs["Group"]
        self.is_auth = request.user and request.user.is_authenticated
        self.is_admin = AdminMember.objects.filter(
            organization__name=self.group_name, member=request.user
        ).exists()
        if view.action == "list" and not self.is_auth and not self.is_admin:
            return False
        else:
            return True

    def has_object_permission(self, request, view, obj):
        """Object permission method."""
        print("enter has_object_permission")
        # only allow the owner to make changes
        user = request.user
        if self.is_admin:
            return True
        if view.action == "destroy":
            print("has_object_permission true: create")
            return True
        elif user == request.user:
            print("has_object_permission true: owner")
            return True  # in practice, an editor will have a profile
        else:
            print("has_object_permission false")
            return False


class UserPermission(permissions.BasePermission):
    """User ViewSet permission class."""

    def has_permission(self, request, view):
        """Global permission method."""
        try:
            # Registration, no permission required.
            if view.action == "create":
                return True
            # Only user can see his details.
            is_legit = view.kwargs["username"] == request.user.username
            is_auth = request.user and request.user.is_authenticated
            return is_legit and is_auth
        except Exception:
            return False
