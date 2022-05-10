"""ViewUserVisibility file of permission package."""
from jjodel.jjodel.models import View, ViewOrgVisibility, ViewUserVisibility
from rest_framework import permissions


class ShareVisibilityPermission(permissions.BasePermission):
    """Check ViewUserVisibility viewset permission."""

    def has_permission(self, request, view):
        """Global auth method."""
        author = view.kwargs["username"]
        if request.user.username != author:
            return False
        return True
