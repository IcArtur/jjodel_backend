"""View serializer file, used to View Model model for DRF."""
from jjodel.view.models import View, ViewRequirement
from rest_framework import serializers


class ViewSerializer(serializers.ModelSerializer):
    """Serializer for View model."""

    author = serializers.SerializerMethodField()

    # Those commented things are to String the BinaryField, don't know if needed.
    # preview_image = BinaryField()

    class Meta:
        """Meta class of ViewSerializer."""

        model = View
        fields = ["name", "preview_image", "description", "is_public", "author", "html"]

    def get_author(self, obj):
        """Get Method serializer."""
        return obj.author.username


class ViewRequirementSerializer(serializers.ModelSerializer):
    """Serializer for ViewRequirement model."""

    class Meta:
        """Meta class of ViewRequirementSerializer."""

        model = ViewRequirement
        fields = "__all__"
