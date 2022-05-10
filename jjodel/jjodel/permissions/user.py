"""User permission"""
from rest_framework import permissions


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
