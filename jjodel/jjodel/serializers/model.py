"""Model serializer file, used to Serialize Model model for DRF."""
from rest_framework import serializers

from ..models import Model


class ModelSerializer(serializers.ModelSerializer):
    """Serializer for Model model."""
    author = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelSerializer."""

        model = Model
        fields = "__all__"

    def get_author(self, obj):
        """Method serializer."""
        return obj.author.username
