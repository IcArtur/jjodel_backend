"""Jjodel admin package."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User
from .model import (  # noqa: F401
    ModelAdmin,
    ModelOrgVisibilityAdmin,
    ModelUserVisibilityAdmin,
    ModelViewpointAdmin,
)
from .organization import OrganizationAdmin  # noqa: F401
from .user import (  # noqa: F401
    AdminMemberAdmin,
    GroupMemberAdmin,
    MembershipRequestAdmin,
)
from .view import (  # noqa: F401
    ViewAdmin,
    ViewOrgVisibilityAdmin,
    ViewRequirementAdmin,
    ViewUserVisibilityAdmin,
)
from .viewpoint import (  # noqa: F401
    ViewpointAdmin,
    ViewpointOrgVisibilityAdmin,
    ViewpointUserVisibilityAdmin,
    ViewpointViewAdmin,
)

admin.site.register(User, UserAdmin)
