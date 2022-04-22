"""Define Jjodel Organization models."""

from django.apps import apps  # noqa: F401
from django.db import connections, models

from jjodel.jjodel.models.model import Model
from jjodel.jjodel.models.user import GroupMember


class Organization(models.Model):
    """Define model for Organization."""

    isPublic = models.BooleanField(verbose_name='Pubblico', default=False)
    openMembership = models.BooleanField(verbose_name='Pubblico', default=False)
    name = models.TextField(verbose_name='Nome')
    mailDomainRequired = models.TextField(verbose_name='Mail Domain')
    bio = models.TextField(verbose_name='Bio')
    owner = models.ForeignKey(GroupMember, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return self.name


class OrganizationVisibility(models.Model):
    """Define model for OrganizationVisibility."""

    readonly = models.BooleanField(verbose_name='Sola lettura', default=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"Visibility {self.organization} - {self.model}"
