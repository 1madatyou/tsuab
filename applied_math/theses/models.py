from django.db import models


class DiplomaThesis(models.Model):
    """Модель дипломной работы"""
    title = models.CharField(verbose_name="Тема")
    file = models.FileField(verbose_name="Файл", upload_to="theses")
    