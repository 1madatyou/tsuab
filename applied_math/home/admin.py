from django.contrib import admin

import admin_thumbnails

from .models import GalleryPhoto


@admin_thumbnails.thumbnail('file')
@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ["title", 'is_show']