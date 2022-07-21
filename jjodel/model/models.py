"""Define Jjodel Model models."""
from django.apps import apps  # noqa: F401
from django.db import models

from jjodel.user.models import User
from jjodel.viewpoint.models import Viewpoint


class Model(models.Model):
    """Define model for Model."""

    is_public = models.BooleanField(verbose_name="Pubblico", default=False)
    content_xml = models.TextField(verbose_name="Content XML")
    namespace = models.TextField(verbose_name="Namespace", null=True, blank=True)
    name = models.TextField(verbose_name="Nome")
    instanceOf = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Return str repr for model."""
        return self.namespace


class ModelViewpoint(models.Model):
    """Define model for ModelViewpoint."""

    viewpoint = models.ForeignKey(Viewpoint, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.model} - {self.viewpoint}"


class ModelOrgVisibility(models.Model):
    """Define model for ModelOrgVisibility."""

    readonly = models.BooleanField(verbose_name="Sola lettura", default=True)
    organization = models.ForeignKey("organization.Organization", on_delete=models.CASCADE)
    model = models.ForeignKey("model.Model", on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.organization} - {self.model} visibility"


class ModelUserVisibility(models.Model):
    """Define model for ModelUserVisibility."""

    readonly = models.BooleanField(verbose_name="Sola lettura", default=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    model = models.ForeignKey("model.Model", on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.user} - {self.model} visibility"
