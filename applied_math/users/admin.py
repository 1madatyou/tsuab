from django.contrib import admin
from django.http import HttpRequest

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'last_login')
    fields = ('email','name', 'patronymic', 'surname', 'is_staff', 'is_active', 'last_login', 'date_joined', 'groups')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
