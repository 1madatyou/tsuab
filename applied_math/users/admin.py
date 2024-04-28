from django.contrib import admin

from .models import User


# @admin.register(User)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'surname', 'patronymic', 'email', 'date_joined')

admin.site.register(User)