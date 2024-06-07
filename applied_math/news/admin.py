
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
import admin_thumbnails

from .models import News, NewsPicture, NewsComment


@admin_thumbnails.thumbnail('picture')
class NewsPictureInline(admin.TabularInline):
    model = NewsPicture

class NewsCommentInline(admin.TabularInline):
    model = NewsComment

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    inlines = [
        NewsPictureInline,
        NewsCommentInline,
    ]

# @admin.register(NewsPicture)
# class NewsPictureAdmin(admin.ModelAdmin):
#     pass
