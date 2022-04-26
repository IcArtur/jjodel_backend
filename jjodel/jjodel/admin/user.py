"""User admin module."""

from django.contrib import admin

from jjodel.jjodel.models import AdminMember, GroupMember, MembershipRequest, \
    UserVisibility


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     """Define User admin."""
#

@admin.register(AdminMember)
class AdminMemberAdmin(admin.ModelAdmin):
    """Define AdminMember admin."""


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    """Define GroupMember admin."""


@admin.register(MembershipRequest)
class MembershipRequestAdmin(admin.ModelAdmin):
    """Define MembershipRequest admin."""


@admin.register(UserVisibility)
class UserVisibilityAdmin(admin.ModelAdmin):
    """Define UserVisibility admin."""

