"""ViewUserVisibility serializer file, used to ViewUserVisibility model for DRF."""
from jjodel.view.models import ViewUserVisibility
from rest_framework import serializers


class ViewUserVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ViewUserVisibility model."""

    user = serializers.SerializerMethodField()
    view = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewUserVisibilitySerializer."""

        model = ViewUserVisibility
        fields = "__all__"

    def get_user(self, obj):
        """Get Method serializer."""
        return obj.user.username

    def get_view(self, obj):
        """Get Method serializer."""
        return obj.view.name
