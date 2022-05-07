"""Model admin module."""

from django.contrib import admin
from jjodel.jjodel.models import Model, ModelViewpoint
from jjodel.jjodel.models.model import ModelOrgVisibility, ModelUserVisibility


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    """Define ModelAdmin admin."""


@admin.register(ModelViewpoint)
class ModelViewpointAdmin(admin.ModelAdmin):
    """Define ModelAdmin admin."""


@admin.register(ModelOrgVisibility)
class ModelOrgVisibilityAdmin(admin.ModelAdmin):
    """Define ModelOrgVisibility admin."""


@admin.register(ModelUserVisibility)
class ModelUserVisibilityAdmin(admin.ModelAdmin):
    """Define ModelUserVisibility admin."""
