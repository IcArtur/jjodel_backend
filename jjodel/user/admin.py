"""User admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from jjodel.user.models import AdminMember, GroupMember, MembershipRequest, User

admin.site.register(User, UserAdmin)


@admin.register(AdminMember)
class AdminMemberAdmin(admin.ModelAdmin):
    """Define AdminMember admin."""


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    """Define GroupMember admin."""


@admin.register(MembershipRequest)
class MembershipRequestAdmin(admin.ModelAdmin):
    """Define MembershipRequest admin."""
