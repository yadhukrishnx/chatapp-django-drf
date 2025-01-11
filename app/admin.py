from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Customize the UserAdmin to show only username and tokens in the list view
class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the list view
    list_display = ('username', 'tokens')

    # Optionally, you can also configure other settings like search fields, etc.
    search_fields = ('username',)

# Register the custom UserAdmin
admin.site.register(User, CustomUserAdmin)
