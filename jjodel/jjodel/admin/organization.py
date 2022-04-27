"""Organization admin module."""

from django.contrib import admin
from jjodel.jjodel.models import Organization, OrganizationVisibility


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Define Organization admin."""


@admin.register(OrganizationVisibility)
class OrganizationVisibilityAdmin(admin.ModelAdmin):
    """Define OrganizationAdmin admin."""
