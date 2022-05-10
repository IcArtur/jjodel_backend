"""ViewpointView serializer file, used to ViewpointView model for DRF."""
from rest_framework import serializers

from ..models import ViewpointView


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
