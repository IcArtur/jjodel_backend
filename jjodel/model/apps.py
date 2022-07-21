"""App file of model."""
from django.apps import AppConfig


class ModelConfig(AppConfig):
    """ModelConfig class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "jjodel.model"
