"""Define Jjodel Viewpoint models."""

from django.apps import apps  # noqa: F401
from django.db import models

from jjodel.jjodel.models.view import View


class Viewpoint(models.Model):
    """Define model for Viewpoint."""

    name = models.CharField(verbose_name="Nome", max_length=255)
    is_public = models.BooleanField(verbose_name="Pubblico", default=False)
    author = models.ForeignKey("jjodel.User", on_delete=models.CASCADE, null=True,
                               blank=True)
    def __str__(self):
        """Return str repr for model."""
        return self.name


class ViewpointView(models.Model):
    """Define model for Viewpointview."""

    viewpoint = models.ForeignKey(Viewpoint, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.viewpoint} - {self.view}"


class ViewpointOrgVisibility(models.Model):
    """Define model for ViewpointOrgVisibility."""

    readonly = models.BooleanField(verbose_name="Sola lettura", default=True)
    organization = models.ForeignKey("jjodel.Organization", on_delete=models.CASCADE)
    viewpoint = models.ForeignKey("jjodel.Viewpoint", on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.organization} - {self.viewpoint}"
