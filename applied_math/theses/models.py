from django.db import models


class DiplomaThesis(models.Model):
    """Модель дипломной работы"""
    title = models.CharField(verbose_name="Тема", max_length=255)
    file = models.FileField(verbose_name="Файл", upload_to="theses")
    date_upload = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)

    class Meta:
        verbose_name_plural = "дипломные работы"
        verbose_name = "дипломная работа"

    def get_formatted_date_upload(self):
        return self.date_upload.strftime('%d.%m.%Y')
    