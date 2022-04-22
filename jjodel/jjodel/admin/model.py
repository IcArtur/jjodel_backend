"""Model admin module."""

from django.contrib import admin

from jjodel.jjodel.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    """Define ModelAdmin admin."""