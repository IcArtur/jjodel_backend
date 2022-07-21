"""Model file of permission package."""
from django.db.models import Q
from jjodel.model.models import Model, ModelOrgVisibility, ModelUserVisibility
from jjodel.organization.models import Organization
from rest_framework import permissions


class ModelPermission(permissions.BasePermission):
    """Check Model viewset permission."""

    def has_permission(self, request, view):
        """Global auth method, check user, authentication and membership."""
        # if view.action == 'update':
        #     return view.kwargs['username'] == request.user.username
        if view.action == "partial_update":
            model = Model.objects.get(namespace__iexact=view.kwargs["namespace"])
            if model.is_public:
                return True
            # First filter organizations in which the user is in
            orgs = request.user.orgs
            # Then check if those orgs has visibility access on model
            orgs_share = ModelOrgVisibility.objects.filter(
                model=model, organization__in=orgs, readonly=False
            ).exists()
            user_share = ModelUserVisibility.objects.filter(
                model=model, user=request.user, readonly=False
            ).exists()
            return request.user == model.author or orgs_share or user_share
        return True

    def has_object_permission(self, request, view, obj):
        """Detail permission check."""
        if view.action == "destroy":
            # Only if the request user is the author the view can be deleted.
            return request.user == obj.author
        if not obj.is_public:
            orgs = Organization.objects.filter(
                Q(groupmember__member=request.user)
                | Q(adminmember__admin=request.user)
                | Q(owner=request.user)
            ).distinct()
            # If ModelUserVisibility exists the user has permission to see it
            user_share = ModelUserVisibility.objects.filter(
                model=obj, user=request.user
            ).exists()
            # If ModelOrgVisibility exists and the user is in it the user has
            # permission to see it
            orgs_share = ModelOrgVisibility.objects.filter(
                model=obj, organization__in=orgs
            ).exists()
            return orgs_share or user_share
        return True
