from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        """Meta class of UserSerializer."""
        model = User
        # Change those fields to display different things on API response.
        fields = ['pk', 'username', 'email', 'first_name', 'last_name']
