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
    

class Manual(models.Model):
    """Модель методического указания"""
    title = models.CharField(verbose_name="Тема", max_length=255)
    file = models.FileField(verbose_name="Файл", upload_to="theses")
    
    author_surname = models.CharField(verbose_name="Фамилия автора", max_length=255)
    author_name = models.CharField(verbose_name="Имя автора", max_length=255)
    author_patronymic = models.CharField(verbose_name="Отчество автора", max_length=255)

    date_upload = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)

    class Meta:
        verbose_name_plural = "методические указания"
        verbose_name = "методическое указание"

    def get_formatted_date_upload(self):
        return self.date_upload.strftime('%d.%m.%Y')
    
    def get_formatted_author_full_name(self):
        return f'{self.author_surname} {self.author_name[0]}.{self.author_patronymic[0]}'