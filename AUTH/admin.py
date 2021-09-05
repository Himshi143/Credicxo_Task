from django.contrib import admin
from .models import AuthUser


@admin.register(AuthUser)
class AuthUser(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'last_login']
    search_fields = ['email']
    list_filter = ['is_superuser', 'is_staff']

    # Override the default save model to hash the raw password.
    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        super(AuthUser, self).save_model(request, obj, form, change)
