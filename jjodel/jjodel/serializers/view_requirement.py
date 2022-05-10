"""ViewRequirement serializer file, used to View Model model for DRAggiungereF."""
from rest_framework import serializers

from ..models import ViewRequirement


class ViewRequirementSerializer(serializers.ModelSerializer):
    """Serializer for ViewRequirement model."""

    class Meta:
        """Meta class of ViewRequirementSerializer."""
        model = ViewRequirement
        fields = "__all__"
