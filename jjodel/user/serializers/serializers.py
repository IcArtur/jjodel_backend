"""User serializer file, used to Serialize User model for DRF."""
from rest_framework import serializers

from jjodel.user.models import MembershipRequest, User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        """Meta class of UserSerializer."""

        model = User
        # Change those fields to display different things on API response.
        fields = ["pk", "username", "email", "first_name", "last_name"]


class MembershipRequestSerializer(serializers.ModelSerializer):
    """Serializer for MembershipRequest model."""

    class Meta:
        """Meta class of MembershipRequestSerializer."""

        model = MembershipRequest
        # Change those fields to display different things on API response.
        fields = ["pk", "sent", "member", "organization"]
