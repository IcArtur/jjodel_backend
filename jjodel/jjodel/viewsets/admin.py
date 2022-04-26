"""Admin REST Api viewset."""
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, status
from rest_framework.response import Response

from jjodel.jjodel.models import User, Organization, GroupMember, AdminMember
from jjodel.jjodel.permissions.member import IsAdminMember
from jjodel.jjodel.serializers.user import UserSerializer


class AdminMembersViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminMember]
    serializer_class = UserSerializer

    def get_queryset(self):
        group_name = self.kwargs['Group']
        return User.objects.filter(adminmember__organization__name=group_name)

    def update(self, request, *args, **kwargs):
        """Update method for AdminMembersViewSet"""
        try:
            user = User.objects.get(username=kwargs['pk'])
            organization = Organization.objects.get(name=kwargs['Group'])
            user_is_admin = AdminMember.objects.filter(admin=request.user,
                                                       organization=organization).exists()
            if user_is_admin:
                AdminMember.objects.update_or_create(admin=user,
                                                     organization=organization)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """Delete method for AdminMembersViewSet"""
        try:
            user = User.objects.get(username=kwargs['pk'])
            organization = Organization.objects.get(name=kwargs['Group'])
            user_is_admin = AdminMember.objects.filter(admin=request.user,
                                                       organization=organization).exists()
            if user_is_admin:
                AdminMember.objects.get(admin=user,
                                        organization=organization).delete()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)
