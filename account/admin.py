from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User, TwoFactorToken

# Register your models here.
auth_admin.UserAdmin.list_display += ('is_two_factor_authenticated',)
auth_admin.UserAdmin.list_filter += ('is_two_factor_authenticated',)
for fieldset, options in auth_admin.UserAdmin.fieldsets:
    if fieldset == 'Permissions':
        options['fields'] = (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_two_factor_authenticated',
            'groups',
            'user_permissions'
            )

class UserAdmin(auth_admin.UserAdmin):
    model = User

class TwoFactorTokenAdmin(admin.ModelAdmin):
    model = TwoFactorToken

admin.site.register(User, UserAdmin)
admin.site.register(TwoFactorToken, TwoFactorTokenAdmin)