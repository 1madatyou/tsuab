import admin_thumbnails

from django.contrib import admin

from .models import News, NewsPicture


@admin_thumbnails.thumbnail('picture')
class NewsPictureInline(admin.TabularInline):
    model = NewsPicture


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        NewsPictureInline,
    ]

# @admin.register(NewsPicture)
# class NewsPictureAdmin(admin.ModelAdmin):
#     pass
