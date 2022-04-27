from jjodel.jjodel.models import AdminMember, GroupMember
from rest_framework import permissions


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
        if view.action == 'list' and not self.is_auth and not self.is_admin:
            return False
        else:
            return True

    def has_object_permission(self, request, view, obj):
        """Object permission method."""
        print('enter has_object_permission')
        # only allow the owner to make changes
        user = request.user
        if self.is_admin:
            return True
        if view.action == 'destroy':
            print('has_object_permission true: create')
            return True
        elif user == request.user:
            print('has_object_permission true: owner')
            return True  # in practice, an editor will have a profile
        else:
            print('has_object_permission false')
            return False
