from django.db import models


class Employee(models.Model):
    """Модель сотрудника"""
    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    patronymic = models.CharField(verbose_name="Отчество", max_length=255)
    position = models.TextField(verbose_name="Должность")
    image = models.FileField(verbose_name="Изображение", upload_to='employees/', null=True, blank=True)
    is_main = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'cотрудник'
        verbose_name_plural = 'cотрудники'

    def get_full_name(self):
        """Возвращает ФИО сотрудника"""
        return f'{self.surname} {self.name} {self.patronymic}'
    
    def set_main(self):
        """Назначает сотрудника главным и отображает его первым на странице 'контакты'"""
        pass
    
    def __str__(self):
        return self.get_full_name()
    

class EmployeeContact(models.Model):
    """Модель контактов сотрудника"""
    employee = models.ForeignKey(
        verbose_name="Контакты", 
        to='contacts.Employee', 
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    title = models.CharField(verbose_name="Тип", max_length=255)
    value = models.CharField(verbose_name="Значение", max_length=255)

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты сотрудника'

    def __str__(self):
        return ''

