from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.forms import CustomUserCreateForm, CustomUserChangeFormInAdmin
from users.models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFormInAdmin
    add_form = CustomUserCreateForm

    list_display = ('name', 'phone', 'full_name', 'date_birth', 'is_active', 'is_admin', 'slug')
    list_display_links = ('name', 'slug')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('phone', 'first_name', 'last_name', 'avatar', 'date_birth', 'slug', 'is_active')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permission', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'password1', 'password2'),
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.unregister(Group)
