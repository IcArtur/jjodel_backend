"""ViewpointOrgVisibility serializer for DRF."""
from jjodel.viewpoint.models import ViewpointOrgVisibility
from rest_framework import serializers


class ViewpointOrgVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ViewpointOrgVisibility model."""

    organization = serializers.SerializerMethodField()
    viewpoint = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewpointOrgVisibilitySerializer."""

        model = ViewpointOrgVisibility
        fields = "__all__"

    def get_organization(self, obj):
        """Get Method serializer."""
        return obj.organization.name

    def get_viewpoint(self, obj):
        """Get Method serializer."""
        return obj.viewpoint.name
