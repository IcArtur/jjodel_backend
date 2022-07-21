"""ViewpointUserVisibility serializer for DRF. """
from rest_framework import serializers

from jjodel.viewpoint.models import ViewpointUserVisibility


class ViewpointUserVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ViewpointUserVisibility model."""

    user = serializers.SerializerMethodField()
    viewpoint = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewpointUserVisibilitySerializer."""

        model = ViewpointUserVisibility
        fields = "__all__"

    def get_user(self, obj):
        """Method serializer."""
        return obj.user.username

    def get_viewpoint(self, obj):
        """Method serializer."""
        return obj.viewpoint.name
