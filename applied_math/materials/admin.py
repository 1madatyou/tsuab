from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    DiplomaThesis,
    Manual,
    EducationalMaterial,
    EducationalMaterialFile,
    EducationalMaterialLink,
)


@admin.register(DiplomaThesis)
class DiplomaThesesAdmin(TranslationAdmin):
    list_display = ["title", "date_upload"]


@admin.register(Manual)
class ManualAdmin(TranslationAdmin):
    list_display = ["title", "date_upload"]


class EducationalMaterialLinkInline(admin.TabularInline):
    model = EducationalMaterialLink
    fields = ["title_en", "title_ru", "href"]


class EducationalMaterialFileInline(admin.TabularInline):
    model = EducationalMaterialFile
    fields = ["title_en", "title_ru", "file"]


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [
        EducationalMaterialLinkInline,
        EducationalMaterialFileInline,
    ]
