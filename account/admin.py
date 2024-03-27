<<<<<<< Updated upstream
from django.contrib import admin  # Import the admin module from Django
from django.contrib.auth.admin import UserAdmin  # Import the UserAdmin class from Django's authentication admin
from .models import Account, UserProfile, Logo  # Import the models Account, UserProfile, and Logo from the current directory
from django.utils.html import format_html  # Import format_html function from Django utils module
=======
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html
>>>>>>> Stashed changes

# Register your models here.

class AccountAdmin(UserAdmin):  # Define a custom admin class AccountAdmin which extends UserAdmin
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')  # Define the fields to display in the list view of admin panel
    list_display_links = ('email', 'first_name', 'last_name')  # Define the fields to link to detail view in the list display
    readonly_fields = ('last_login', 'date_joined')  # Define fields that are readonly in admin panel
    ordering = ('-date_joined',)  # Define ordering of records in the admin panel

    filter_horizontal = () 
    list_filter = ()  
    fieldsets = ()  

class UserProfileAdmin(admin.ModelAdmin):  # Define a custom admin class UserProfileAdmin
    def thumbnail(self, object):  # Define a method to display thumbnail of profile picture
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))  # Format HTML to display image
    thumbnail.short_description = 'Profile Picture'  # Define short description for thumbnail column
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')  # Define the fields to display in the list view of admin panel

admin.site.register(Account, AccountAdmin)  # Register the Account model with the custom admin class AccountAdmin
admin.site.register(UserProfile, UserProfileAdmin)  # Register the UserProfile model with the custom admin class UserProfileAdmin
admin.site.register(Logo)  # Register the Logo model with the default admin options

<<<<<<< Updated upstream
=======
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
>>>>>>> Stashed changes
