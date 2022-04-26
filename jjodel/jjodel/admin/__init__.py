"""Jjodel admin package."""

from .view import ViewAdmin, ViewOrgVisibilityAdmin, ViewRequirementAdmin, ViewUserVisibilityAdmin  # noqa: F401
from .viewpoint import ViewpointAdmin, ViewpointViewAdmin  # noqa: F401
from .model import ModelAdmin, ModelViewpointAdmin  # noqa: F401
from .user import AdminMemberAdmin, GroupMemberAdmin, MembershipRequestAdmin, \
    UserVisibilityAdmin
from .organization import OrganizationAdmin, OrganizationVisibilityAdmin  # noqa: F401


from django.contrib.auth.admin import UserAdmin
from ..models import User
from django.contrib import admin

admin.site.register(User, UserAdmin)
