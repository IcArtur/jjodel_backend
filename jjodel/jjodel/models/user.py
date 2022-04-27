"""Define Jjodel User models."""
from datetime import datetime

from django.apps import apps  # noqa: F401
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Define model for User."""

    bio = models.TextField(verbose_name="Bio", null=True, blank=True)


class AdminMember(models.Model):
    """Define model for AdminMember."""

    since = models.DateField(editable=False, null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey("jjodel.Organization", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """On save set created."""
        if not self.id:
            self.since = datetime.now().date()
        return super(AdminMember, self).save(*args, **kwargs)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.admin} - {self.organization}"


class GroupMember(models.Model):
    """Define model for GroupMember."""

    since = models.DateField(editable=False, null=True, blank=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_fk = models.ForeignKey("jjodel.Organization", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Oreturn Response(status=status.HTTP_403_FORBIDDEN)n save set created."""
        if not self.id:
            self.since = datetime.now().date()
        return super(GroupMember, self).save(*args, **kwargs)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.member} - {self.organization_fk}"


class MembershipRequest(models.Model):
    """Define model for MembershipRequest."""

    sent = models.DateField(editable=False, null=True, blank=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey("jjodel.Organization", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """On save set created."""
        if not self.id:
            self.sent = datetime.now().date()
        return super(MembershipRequest, self).save(*args, **kwargs)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.member} - {self.organization}"


class UserVisibility(models.Model):
    """Define model for UserVisibility."""

    readonly = models.BooleanField(verbose_name="Sola lettura", default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey("jjodel.Model", on_delete=models.CASCADE)

    def __str__(self):
        """Return str repr for model."""
        return f"{self.user} - {self.model}"
