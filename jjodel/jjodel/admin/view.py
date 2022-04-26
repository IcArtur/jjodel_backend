"""View admin module."""

from django.contrib import admin

from jjodel.jjodel.models import View, ViewOrgVisibility, ViewRequirement, \
    ViewUserVisibility


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    """Define View admin."""


@admin.register(ViewOrgVisibility)
class ViewOrgVisibilityAdmin(admin.ModelAdmin):
    """Define ViewOrgVisibility admin."""


@admin.register(ViewRequirement)
class ViewRequirementAdmin(admin.ModelAdmin):
    """Define ViewRequirement admin."""


@admin.register(ViewUserVisibility)
class ViewUserVisibilityAdmin(admin.ModelAdmin):
    """Define ViewUserVisibility admin."""
