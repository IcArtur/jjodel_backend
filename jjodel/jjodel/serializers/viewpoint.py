"""Viewpoint serializer file, used to Viewpoint Model model for DRF."""
from rest_framework import serializers

from ..models import Viewpoint


class ViewpointSerializer(serializers.ModelSerializer):
    """Serializer for Viewpoint model."""

    class Meta:
        """Meta class of ViewpointSerializer."""

        model = Viewpoint
        fields = "__all__"
