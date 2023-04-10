from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from users import models


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'phone_number')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

# class CustomUserAdmin(UserAdmin):
#     fieldsets = '__all__'


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'phone_number',
                'user_type',
            )
        }),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(models.CustomUser, CustomUserAdmin)
