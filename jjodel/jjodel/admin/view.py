"""View admin module."""

from django.contrib import admin

from jjodel.jjodel.models import View


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    """Define View admin."""
