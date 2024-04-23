from django.db import models


class NewsPicture(models.Model):
    """Модель изображения новости"""
    picture = models.FileField(verbose_name="Изображение")
    # title = models.CharField(verbose_name="", max_length=256, null=True)


class News(models.Model):
    """Модель новости"""
    title = models.TextField(verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст новости")
    pictures = models.ManyToManyField(verbose_name="Изображения", to=NewsPicture)



    
