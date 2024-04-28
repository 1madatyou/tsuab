from django.db import models


class News(models.Model):
    """Модель новости"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст новости")

    def __str__(self):
        return f"Новость: {self.title}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsPicture(models.Model):
    """Модель изображения новости"""
    picture = models.FileField(verbose_name="Изображение")
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return "Изображение новости"
    
    class Meta:
        verbose_name = "Изображение новости"
        verbose_name_plural = "Изображения новостей"




    
