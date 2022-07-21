"""ModelUserVisibility serializer for DRF."""
from jjodel.model.models import ModelUserVisibility
from rest_framework import serializers


class ModelUserVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ModelUserVisibility model."""

    user = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelUserVisibilitySerializer."""

        model = ModelUserVisibility
        fields = "__all__"

    def get_user(self, obj):
        """Get Method serializer."""
        return obj.user.username

    def get_model(self, obj):
        """Get Method serializer."""
        return obj.model.namespace
