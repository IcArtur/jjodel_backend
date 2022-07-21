"""Model serializer file, used to Serialize Model model for DRF."""
from jjodel.model.models import Model, ModelViewpoint
from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):
    """Serializer for Model model."""

    author = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelSerializer."""

        model = Model
        fields = "__all__"

    def get_author(self, obj):
        """Get Method serializer."""
        return obj.author.username


class ModelViewpointSerializer(serializers.ModelSerializer):
    """Serializer for ModelViewpoimt model."""

    viewpoint = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ModelViewpointSerializer."""

        model = ModelViewpoint
        fields = "__all__"

    def get_viewpoint(self, obj):
        """Get Method serializer."""
        return obj.viewpoint.name

    def get_model(self, obj):
        """Get Method serializer."""
        return obj.model.namespace
