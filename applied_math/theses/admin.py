from django.contrib import admin

from .models import DiplomaThesis


@admin.register(DiplomaThesis)
class DiplomaThesesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_upload']