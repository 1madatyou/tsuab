from django.db import models


class GalleryPhoto(models.Model):
    """Модель изображения из галереи"""

    title = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(verbose_name="Файл", upload_to="gallery/")
    is_show = models.BooleanField(
        verbose_name="Отображается",
        default=True,
        choices=[(True, "Да"), (False, "Нет")],
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения галереи"
