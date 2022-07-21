"""ModelUserVisibility serializer for DRF. """
from rest_framework import serializers

from jjodel.model.models import ModelUserVisibility


class ModelUserVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ModelUserVisibility model."""

    user = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelUserVisibilitySerializer."""

        model = ModelUserVisibility
        fields = "__all__"

    def get_user(self, obj):
        """Method serializer."""
        return obj.user.username

    def get_model(self, obj):
        """Method serializer."""
        return obj.model.namespace
