from django.db import models


class Schedule(models.Model):
    """Одиночная модель расписания"""
    file = models.FileField(verbose_name="Файл", upload_to="schedule")
    date_updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)

    def __str__(self):
        return 'Расписание'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

        