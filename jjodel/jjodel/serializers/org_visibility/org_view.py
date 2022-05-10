"""ViewOrgVisibility serializer file, used to ViewOrgVisibility model for DRF."""
from jjodel.jjodel.models import ViewOrgVisibility
from rest_framework import serializers


class ViewOrgVisibilitySerializer(serializers.ModelSerializer):
    """Serializer for ViewOrgVisibility model."""

    organization = serializers.SerializerMethodField()
    view = serializers.SerializerMethodField()

    class Meta:
        """Meta class of ViewOrgVisibilitySerializer."""

        model = ViewOrgVisibility
        fields = "__all__"

    def get_organization(self, obj):
        """Method serializer."""
        return obj.organization.name

    def get_view(self, obj):
        """Method serializer."""
        return obj.view.name
