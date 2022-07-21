"""View apps file."""
from django.apps import AppConfig


class ViewConfig(AppConfig):
    """ViewConfig class of view package."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "jjodel.view"
