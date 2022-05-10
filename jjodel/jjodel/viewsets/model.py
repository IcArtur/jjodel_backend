"""Model REST Api viewset."""
from jjodel.jjodel.models import AdminMember, GroupMember, Model, Organization, User
from jjodel.jjodel.permissions.model import ModelPermission
from jjodel.jjodel.serializers.model import ModelSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet ViewSet."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [ModelPermission]
    serializer_class = ModelSerializer
    lookup_field = "namespace"

    def get_queryset(self):
        """Define queryset for ModelViewSet class. This filters modela."""
        if self.action == "list":
            # I considered the bool value true when '1' is passed.
            is_regexp = self.request.query_params.get("regex") == "1"
            namespace = self.request.query_params.get("namespace") or None
            if is_regexp:
                qs = Model.objects.filter(namespace__regex=rf"{namespace}")
            else:
                qs = Model.objects.filter(namespace__icontains=namespace)
        else:
            qs = Model.objects.filter(namespace__iexact=self.kwargs["namespace"])
        return qs

    def partial_update(self, request, *args, **kwargs):
        """PATCH Update Model."""
        try:
            d = self.get_data_dict(request.data)
            model = Model.objects.filter(namespace=kwargs["namespace"])
            if not model.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"detail": "Model does not exists."},
                )
            model.update(**d)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """PUT method for model."""
        try:
            d = self.get_data_dict(request.data)
            if Model.objects.filter(namespace=d["namespace"]).exists():
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={"detail": "Model namespace is already taken"},
                )
            model = Model.objects.create(**d)
            model.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_data_dict(data):
        """Create dict from data"""
        d = {"namespace": data["namespace"]}
        if data.get("isPublic"):
            d["is_public"] = data["isPublic"] == "1"
        if data.get("content_xml"):
            d["content_xml"] = data["content_xml"]
        if data.get("name"):
            d["name"] = data["name"]
        if data.get("instanceOf"):
            instance_of = Model.objects.get(namespace=data["instanceOf"])
            d["instanceOf"] = instance_of
        if data.get("author"):
            # Update by username
            author = User.objects.get(username=data["author"])
            d["author"] = author
        return d
