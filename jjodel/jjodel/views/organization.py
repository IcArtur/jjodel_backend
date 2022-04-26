"""Organization REST Api view."""
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response

from jjodel.jjodel.models import User, Organization, GroupMember, AdminMember
from jjodel.jjodel.permissions.organization import IsGroupMember
from jjodel.jjodel.serializers.user import UserSerializer


class GroupMembersViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsGroupMember]
    serializer_class = UserSerializer

    def get_queryset(self):
        group_name = self.kwargs['Group']
        return User.objects.filter(groupmember__organization_fk__name=group_name)

    def update(self, request, *args, **kwargs):
        """Update method for GroupMembersView"""
        try:
            user = User.objects.get(username=kwargs['pk'])
            organization = Organization.objects.get(name=kwargs['Group'])
            user_is_admin = AdminMember.objects.filter(admin=request.user,
                                                       organization=organization).exists()
            if organization.openMembership or user_is_admin:
                GroupMember.objects.update_or_create(member=user,
                                                     organization_fk=organization)
            else:
                return Response(
                    {"status_code": 403})
        except Exception:
            return Response(
                {"status_code": 404})
        return Response({"status_code": 200})

    def destroy(self, request, *args, **kwargs):
        """Delete method for GroupMembersView"""
        try:
            user = User.objects.get(username=kwargs['pk'])
            organization = Organization.objects.get(name=kwargs['Group'])
            user_is_admin = AdminMember.objects.filter(admin=request.user,
                                                       organization=organization).exists()
            if request.user == user or user_is_admin:
                GroupMember.objects.get(member=user,
                                        organization_fk=organization).delete()
            else:
                return Response(
                    {"status_code": 403})
        except Exception:
            return Response({"status_code": 404})
        return Response({"status_code": 200})
