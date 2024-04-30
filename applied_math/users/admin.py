from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'last_login')
    fields = ('email','name', 'patronymic', 'surname', 'is_staff', 'is_active', 'last_login', 'date_joined', 'groups')
