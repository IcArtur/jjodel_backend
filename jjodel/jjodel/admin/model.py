"""Model admin module."""

from django.contrib import admin

from jjodel.jjodel.models import Model, ModelViewpoint


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    """Define ModelAdmin admin."""


@admin.register(ModelViewpoint)
class ModelViewpointAdmin(admin.ModelAdmin):
    """Define ModelAdmin admin."""
