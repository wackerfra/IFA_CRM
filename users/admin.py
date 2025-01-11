from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for managing users.
    """
    fieldsets = UserAdmin.fieldsets + (
        # You can add custom fields here if needed
        # ('Additional Info', {'fields': ('custom_field',)}),
    )
