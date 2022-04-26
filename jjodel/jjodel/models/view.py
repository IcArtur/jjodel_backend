"""Define Jjodel View models."""

from django.apps import apps  # noqa: F401
from django.db import connections, models


class View(models.Model):
    """Define model for View."""

    preview_image = models.BinaryField(verbose_name='Preview Immagine', null=True, blank=True)
    description = models.TextField(verbose_name='Descrizione')
    is_public = models.BooleanField(verbose_name='Pubblico', default=False)
    html = models.TextField(verbose_name='Testo HTML', null=True, blank=True)

    def __str__(self):
        """Return str repr for model."""
        return self.description


class ViewOrgVisibility(models.Model):
    """Define model for ViewOrgVisibility."""

    readonly = models.BooleanField(verbose_name='Sola lettura', default=True)
    organization = models.ForeignKey("jjodel.Organization", on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.organization} - {self.view}"


class ViewRequirement(models.Model):
    """Define model for ViewRequirement."""

    oclString = models.TextField(verbose_name='Commento')
    comment = models.TextField(verbose_name='Commento', null=True, blank=True)
    view = models.ForeignKey(View, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"Requirement - {self.view}"


class ViewUserVisibility(models.Model):
    """Define model for ViewUserVisibility."""

    readonly = models.BooleanField(verbose_name='Sola lettura', default=True)
    user = models.ForeignKey("jjodel.User", on_delete=models.CASCADE)
    view = models.ForeignKey("jjodel.View", on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"Visibility - {self.user} - {self.view}"
