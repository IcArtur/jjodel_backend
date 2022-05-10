"""View serializer file, used to View Model model for DRF."""
from rest_framework import serializers

from ..models import View

# class BinaryField(serializers.Field):
#     def to_representation(self, value):
#         return value.tobytes()
#
#     def to_internal_value(self, value):
#         return value.encode('utf-8')


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
        """Method serializer."""
        return obj.author.username
