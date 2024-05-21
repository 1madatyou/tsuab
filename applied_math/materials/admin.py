from django.contrib import admin

from .models import DiplomaThesis, Manual


@admin.register(DiplomaThesis)
class DiplomaThesesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_upload']


@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_upload']