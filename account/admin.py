from django.contrib import admin

from .models import User, TwoFactorToken

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = User

class TwoFactorTokenAdmin(admin.ModelAdmin):
    model = TwoFactorToken

admin.site.register(User, UserAdmin)
admin.site.register(TwoFactorToken, TwoFactorTokenAdmin)