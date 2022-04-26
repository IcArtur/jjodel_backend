from rest_framework import serializers

from ..models import Model


class ModelSerializer(serializers.ModelSerializer):
    """Serializer for Model model."""
    class Meta:
        """Meta class of ModelSerializer."""
        model = Model
        fields = '__all__'

