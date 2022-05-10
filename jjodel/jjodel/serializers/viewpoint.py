"""Viewpoint serializer file, used to Viewpoint Model model for DRF."""
from rest_framework import serializers

from ..models import Viewpoint


class ViewpointSerializer(serializers.ModelSerializer):
    """Serializer for Viewpoint model."""

    author = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewpointSerializer."""

        model = Viewpoint
        fields = ["pk", "name", "is_public", "author"]

    def get_author(self, obj):
        """Method serializer."""
        return obj.author.username
