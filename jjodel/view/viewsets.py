"""View REST Api viewset."""
from jjodel.organization.permissions import ShareVisibilityPermission
from jjodel.user.models import User
from jjodel.view.models import View, ViewRequirement
from jjodel.view.permissions import ViewPermission
from jjodel.view.serializers import ViewRequirementSerializer, ViewSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ViewViewSet(viewsets.ModelViewSet):
    """View ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewSerializer
    permission_classes = [ViewPermission]
    lookup_field = "name"

    def get_queryset(self):
        """Define queryset for ViewViewSet class. This filters View."""
        # I considered the bool value true when 1 is passed.
        if self.action == "list":
            is_regexp = self.request.query_params.get("regex") == "1"
            vpname = self.request.query_params.get("vpname") or None
            viewname = self.request.query_params.get("viewname") or ""
            author = self.request.query_params.get("author") or ""
            if is_regexp:
                qs = View.objects.filter(
                    name__regex=rf"{viewname}", author__username__icontains=author
                )
            else:
                qs = View.objects.filter(
                    name__icontains=viewname, author__username__icontains=author
                )
            if vpname:
                qs = qs.filter(viewpointview__viewpoint__name__icontains=vpname)
        else:
            qs = View.objects.filter(
                name__iexact=self.kwargs["name"],
                author__username__iexact=self.kwargs["username"],
            )
        return qs

    def partial_update(self, request, *args, **kwargs):
        """Update View."""
        try:
            d = self.get_data_dict(request.data)
            view_qs = View.objects.filter(
                name=kwargs["name"], author__username=kwargs["username"]
            )
            if not view_qs.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"detail": "View does not exists."},
                )
            view_qs.update(**d)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """PUT method for view."""
        try:
            d = self.get_data_dict(request.data)
            if View.objects.filter(name=d["name"]).exists():
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={"detail": "View name is already taken"},
                )
            view_object = View.objects.create(**d)
            view_object.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_data_dict(data):
        """Create dict from data."""
        d = {"name": data["viewname"]}
        if data.get("isPublic"):
            d["is_public"] = data["isPublic"] == "1"
        if data.get("author"):
            # Update by username
            author = User.objects.get(username=data["author"])
            d["author"] = author
        if data.get("preview_image"):
            encoded_preview = data["preview_image"].encode("utf-8")
            d["preview_image"] = encoded_preview
        if data.get("html"):
            d["html"] = data["html"]
        if data.get("description"):
            d["description"] = data["description"]
        return d


class ViewRequirementViewSet(viewsets.ModelViewSet):
    """ViewUserVisibility ViewSet."""

    authentication_classes = [TokenAuthentication]
    serializer_class = ViewRequirementSerializer
    permission_classes = [ShareVisibilityPermission]

    def get_queryset(self):
        """Define queryset for ViewViewSet class. This filters View."""
        author = self.kwargs["username"]
        view = self.kwargs["viewname"]
        return ViewRequirement.objects.filter(
            view__name=view, view__author__username=author
        )

    def create(self, request, *args, **kwargs):
        """POST method, create."""
        try:
            d = self.get_data_dict(request.data)
            view = View.objects.get(name=kwargs["viewname"])
            ViewRequirement.objects.create(**d, view=view)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """PATCH method, update."""
        try:
            d = self.get_data_dict(request.data)
            ViewRequirement.objects.filter(pk=kwargs["pk"]).update(**d)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_data_dict(data):
        """Create dict from data."""
        d = {"oclString": data["oclString"]}
        if data.get("comment"):
            d["comment"] = data["comment"]
        return d
