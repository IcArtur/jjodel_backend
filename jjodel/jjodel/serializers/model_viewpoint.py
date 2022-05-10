"""ModelViewpoimt serializer file, used to VieViewUserVisibility, \
    ViewRequirement, w ModelViewpoimt model for DRF."""
from rest_framework import serializers

from ..models import ModelViewpoint


class ModelViewpointSerializer(serializers.ModelSerializer):
    """Serializer for ModelViewpoimt model."""
    viewpoint = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelViewpointSerializer."""
        model = ModelViewpoint
        fields = "__all__"

    def get_viewpoint(self, obj):
        """Method serializer."""
        return obj.viewpoint.name

    def get_model(self, obj):
        """Method serializer."""
        return obj.model.namespace
