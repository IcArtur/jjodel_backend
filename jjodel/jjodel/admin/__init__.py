"""Jjodel admin package."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User
from .model import ModelAdmin, ModelViewpointAdmin, ModelOrgVisibilityAdmin, \
    ModelUserVisibilityAdmin  # noqa: F401
from .organization import OrganizationAdmin, OrganizationVisibilityAdmin  # noqa: F401
from .user import (  # noqa: F401
    AdminMemberAdmin,
    GroupMemberAdmin,
    MembershipRequestAdmin,
    UserVisibilityAdmin,
)
from .view import (  # noqa: F401
    ViewAdmin,
    ViewOrgVisibilityAdmin,
    ViewRequirementAdmin,
    ViewUserVisibilityAdmin,
)
from .viewpoint import ViewpointAdmin, ViewpointViewAdmin, ViewpointOrgVisibilityAdmin, \
    ViewpointUserVisibilityAdmin  # noqa: F401

admin.site.register(User, UserAdmin)
