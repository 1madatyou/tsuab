from django.contrib import admin

from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    actions = None

    def has_add_permission(self, request):
        if Schedule.objects.exists():
            return False
        return True
