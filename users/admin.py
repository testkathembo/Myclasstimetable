from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Display these fields in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    
    # Fields to include in the search bar
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role')
    
    # Add filtering options in the admin sidebar
    list_filter = ('role', 'is_staff', 'is_active')
    
    # Pagination: Number of users displayed per page
    list_per_page = 10

    # Group fields in the detail view
    fieldsets = (
        (None, {"fields": ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),  # Keep this here but make it read-only
        ('Role and Faculty', {'fields': ('role', 'faculty_id')}),
    )

    # Mark 'date_joined' as read-only
    readonly_fields = ('date_joined',)

    # Fields to show when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'phone', 'role', 'faculty_id', 'password1', 'password2'),
        }),
    )