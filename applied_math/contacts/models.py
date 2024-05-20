from django.db import models


class Employee(models.Model):
    """Модель сотрудника"""
    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    patronymic = models.CharField(verbose_name="Отчество", max_length=255)
    position = models.TextField(verbose_name="Должность")
    image = models.FileField(verbose_name="Изображение", upload_to='employees/', null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name = 'Сотрудники'

