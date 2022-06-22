"""Viewpoint REST Api viewset."""
from jjodel.jjodel.models import User, Viewpoint
from jjodel.jjodel.permissions.viewpoint import ViewpointPermission
from jjodel.jjodel.serializers.viewpoint import ViewpointSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ViewpointViewSet(viewsets.ModelViewSet):
    """Viewpoint ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewpointSerializer
    permission_classes = [ViewpointPermission]
    lookup_field = "name"

    def get_queryset(self):
        """Define queryset for ViewpointViewSet class. This filters organizations."""
        # I considered the bool value true when 1 is passed.
        if self.action == "list":
            is_regexp = self.request.query_params.get("regex") == "1"
            vpname = self.request.query_params.get("vpname") or ""
            author = self.request.query_params.get("author") or ""
            if is_regexp:
                qs = Viewpoint.objects.filter(
                    name__regex=rf"{vpname}", author__username__icontains=author
                )
            else:
                qs = Viewpoint.objects.filter(
                    name__icontains=vpname, author__username__icontains=author
                )
        else:
            qs = Viewpoint.objects.filter(
                name__iexact=self.kwargs["name"],
                author__username__iexact=self.kwargs["username"],
            )
        return qs

    def partial_update(self, request, *args, **kwargs):
        """Update Viewpoint."""
        try:
            d = self.get_data_dict(request.data)
            vp = Viewpoint.objects.filter(name=kwargs["name"])
            if not vp.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"detail": "Viewpoint does not exists."},
                )
            vp.update(**d)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """PUT method for viewpoint."""
        try:
            d = self.get_data_dict(request.data)
            if Viewpoint.objects.filter(name=d["name"]).exists():
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={"detail": "Viewpoint name is already taken"},
                )
            vp = Viewpoint.objects.create(**d)
            vp.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_data_dict(data):
        """Create dict from data"""
        d = {"name": data["vpname"]}
        if data.get("isPublic"):
            d["is_public"] = data["isPublic"] == "1"
        if data.get("author"):
            # Update by username
            author = User.objects.get(username=data["author"])
            d["author"] = author
        if data.get("coordinates"):
            d["coordinates"] = data["coordinates"]
        return d
