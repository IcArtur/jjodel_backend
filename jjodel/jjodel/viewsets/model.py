"""Model REST Api viewset."""
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from jjodel.jjodel.models import Organization, User, GroupMember, AdminMember
from jjodel.jjodel.serializers.model import ModelSerializer


class ModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ModelSerializer
