"""Viewpoint admin module."""

from django.contrib import admin
from jjodel.viewpoint.models import (
    Viewpoint,
    ViewpointOrgVisibility,
    ViewpointUserVisibility,
    ViewpointView,
)


@admin.register(Viewpoint)
class ViewpointAdmin(admin.ModelAdmin):
    """Define Viewpoint admin."""


@admin.register(ViewpointView)
class ViewpointViewAdmin(admin.ModelAdmin):
    """Define ViewpointView admin."""


@admin.register(ViewpointOrgVisibility)
class ViewpointOrgVisibilityAdmin(admin.ModelAdmin):
    """Define ViewpointOrgVisibility admin."""


@admin.register(ViewpointUserVisibility)
class ViewpointUserVisibilityAdmin(admin.ModelAdmin):
    """Define ViewpointUserVisibility admin."""
