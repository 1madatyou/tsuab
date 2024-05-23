
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
import admin_thumbnails

from .models import News, NewsPicture


@admin_thumbnails.thumbnail('picture')
class NewsPictureInline(admin.TabularInline):
    model = NewsPicture


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    inlines = [
        NewsPictureInline,
    ]

# @admin.register(NewsPicture)
# class NewsPictureAdmin(admin.ModelAdmin):
#     pass
