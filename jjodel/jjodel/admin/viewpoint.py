"""Viewpoint admin module."""

from django.contrib import admin

from jjodel.jjodel.models import Viewpoint


@admin.register(Viewpoint)
class ViewpointAdmin(admin.ModelAdmin):
    """Define Viewpoint admin."""
