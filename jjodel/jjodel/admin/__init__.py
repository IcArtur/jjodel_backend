"""Jjodel admin package."""

from .view import ViewAdmin  # noqa: F401
from .viewpoint import ViewpointAdmin  # noqa: F401
from .model import ModelAdmin  # noqa: F401
# from .user import UserAdmin  # noqa: F401
from django.contrib.auth.admin import UserAdmin
from .organization import OrganizationAdmin  # noqa: F401
from ..models import User
from django.contrib import admin

admin.site.register(User, UserAdmin)



