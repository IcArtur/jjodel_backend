"""User REST Api viewset."""
from jjodel.jjodel.models import User
from jjodel.jjodel.permissions.user import UserPermission
from jjodel.jjodel.serializers.user import UserSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """UserViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    lookup_field = "username"
    queryset = User.objects.filter()

    def create(self, request, *args, **kwargs):
        """Register method."""
        try:
            d = self.get_data_dict(request.data)
            user = User.objects.create_user(**d)
            user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """Update user."""
        try:
            d = self.get_data_dict(request.data)
            user = User.objects.filter(username=request.data["username"])
            user.update(**d)
            if request.data.get("password"):
                # Need and user instance to change pass, can'd do it on slice queryset.
                user_instance = User.objects.get(username=request.data["username"])
                user_instance.set_password(request.data["password"])
                user_instance.save()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_data_dict(data):
        """Create dict from data"""
        d = {"username": data["username"]}
        if data.get("name"):
            d["first_name"] = data["name"]
        if data.get("surname"):
            d["last_name"] = data["surname"]
        if data.get("bio"):
            d["bio"] = data["bio"]
        if data.get("mail"):
            d["email"] = data["mail"]
        if data.get("password"):
            d["password"] = data["password"]
        return d
