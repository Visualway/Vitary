from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    """
    Including the profile model in the user model by inline admin
    """
    model = Profile
    readonly_fields = ['profile_image', 'follower_count', 'following_count', 'auth_token']
    fields = [
        'profile_image',
        'image',
        'email_notif',
        'verified',
        'bio',
        'follower_count',
        'following_count',
        'header_image',
        'badges',
        'status',
        'auth_token'
    ]
    can_delete = False


def make_verified(self, request, queryset):
    """
    Make Selected users profile verified
    """
    for user in queryset:
        user.profile.verified = True
        user.profile.save()
    self.message_user(request, "Selected users verified")


make_verified.short_description = "Make Selected Users Verified"


def make_unverified(self, request, queryset):
    """  
    Make Selected users profile unverified
    """
    for user in queryset:
        user.profile.verified = False
        user.profile.save()
    self.message_user(request, "Selected users unverified")


make_unverified.short_description = "Make Selected Users Unverified"


class UserAdmin(BaseUserAdmin):
    """
    Adding the profile inline in user model admin
    """
    inlines = [ProfileInline,]
    actions = [make_verified, make_unverified]


# Registering the model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
