"""Organization admin module."""

from django.contrib import admin
from jjodel.jjodel.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Define Organization admin."""

    readonly_fields = ("owner",)
