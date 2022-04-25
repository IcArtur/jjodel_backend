"""Define Jjodel Model models."""
from django.apps import apps  # noqa: F401
from django.db import models

from jjodel.jjodel.models.user import User
from jjodel.jjodel.models.viewpoint import Viewpoint


class Model(models.Model):
    """Define model for Model."""

    isPublic = models.BooleanField(verbose_name='Pubblico', default=False)
    content_xml = models.TextField(verbose_name='Content XML')
    name = models.TextField(verbose_name='Nome')
    instanceOf = models.ForeignKey('self', on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return self.name


class ModelViewpoint(models.Model):
    """Define model for ModelViewpoint."""

    viewpoint = models.ForeignKey(Viewpoint, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.model} - {self.viewpoint}"
