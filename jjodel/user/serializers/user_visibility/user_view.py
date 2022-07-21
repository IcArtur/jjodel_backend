"""ViewUserVisibility serializer file, used to ViewUserVisibility model for DRF."""
from rest_framework import serializers

from jjodel.view.models import ViewUserVisibility


class ViewUserVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ViewUserVisibility model."""

    user = serializers.SerializerMethodField()
    view = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewUserVisibilitySerializer."""

        model = ViewUserVisibility
        fields = "__all__"

    def get_user(self, obj):
        """Method serializer."""
        return obj.user.username

    def get_view(self, obj):
        """Method serializer."""
        return obj.view.name
