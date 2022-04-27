"""Organization serializer file, used to Organization model for DRF."""
from rest_framework import serializers

from ..models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for Organization model."""

    class Meta:
        """Meta class of OrganizationSerializer."""

        model = Organization
        # Change those fields to display different things on API response.
        fields = ["pk", "name", "isPublic", "openMembership", "mailDomainRequired",
                  "owner"]
