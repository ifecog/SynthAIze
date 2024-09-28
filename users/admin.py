from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from users.forms import UserCreationForm, UserChangeForm
from users.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.profile_picture.url))
        except:
            pass

    thumbnail.short_description = 'photo'

    
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('thumbnail', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active',)
    list_display_links = ('thumbnail', 'email')
    list_filter = ('email', 'role', 'is_staff', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('profile_picture', 'email', 'first_name', 'last_name', 'role', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
