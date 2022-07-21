"""Viewpoint serializer file, used to Viewpoint Model model for DRF."""
from rest_framework import serializers

from jjodel.viewpoint.models import Viewpoint, ViewpointView


class ViewpointSerializer(serializers.ModelSerializer):
    """Serializer for Viewpoint model."""

    author = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewpointSerializer."""

        model = Viewpoint
        fields = ["pk", "name", "is_public", "author", "coordinates"]

    def get_author(self, obj):
        """Method serializer."""
        return obj.author.username


class ViewpointViewSerializer(serializers.ModelSerializer):
    """Serializer for ViewpointView model."""
    viewpoint = serializers.SerializerMethodField()
    view = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewpointViewSerializer."""
        model = ViewpointView
        fields = "__all__"

    def get_viewpoint(self, obj):
        """Method serializer."""
        return obj.viewpoint.name

    def get_view(self, obj):
        """Method serializer."""
        return obj.view.name
