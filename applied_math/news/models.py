from django.db import models


class News(models.Model):
    """Модель новости"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст новости")
    date_created = models.DateTimeField(verbose_name="Дата создания", editable=False, auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_last_picture_url(self):
        """Возвращает url последнего изображения новости"""
        return self.pictures.last().picture.url
    
    def get_formatted_date_created(self):
        """Возвращает отформатированную дату создания новости"""
        return self.date_created.strftime("%d.%m.%Y")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-id']


class NewsPicture(models.Model):
    """Модель изображения новости"""
    picture = models.FileField(verbose_name="Изображение")
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return "Изображение новости"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"




    
