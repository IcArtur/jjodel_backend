"""View serializer file, used to View Model model for DRF."""
from rest_framework import serializers

from ..models import View


class ViewSerializer(serializers.ModelSerializer):
    """Serializer for View model."""
    author = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewSerializer."""
        model = View
        fields = ['name','preview_image', 'description', 'is_public', 'author', 'html']

    def get_author(self, obj):
        """Method serializer."""
        return obj.author.username
