"""ModelOrgVisibility serializer for DRF. """
from rest_framework import serializers

from jjodel.jjodel.models.model import ModelOrgVisibility


class ModelOrgVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ModelOrgVisibility model."""
    organization = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelOrgVisibilitySerializer."""
        model = ModelOrgVisibility
        fields = '__all__'

    def get_organization(self, obj):
        """Method serializer."""
        return obj.organization.name

    def get_model(self, obj):
        """Method serializer."""
        return obj.model.namespace
