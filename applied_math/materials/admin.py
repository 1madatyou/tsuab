from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import DiplomaThesis, Manual


@admin.register(DiplomaThesis)
class DiplomaThesesAdmin(TranslationAdmin):
    list_display = ['title', 'date_upload']


@admin.register(Manual)
class ManualAdmin(TranslationAdmin):
    list_display = ['title', 'date_upload']