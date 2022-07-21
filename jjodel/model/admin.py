"""Model admin module."""

from django.contrib import admin
from django.contrib.auth.models import Group
from jjodel.model.models import (
    Model,
    ModelOrgVisibility,
    ModelUserVisibility,
    ModelViewpoint,
)


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


# Unregister Group from admin dashboard
admin.site.unregister(Group)
