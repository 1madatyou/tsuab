from django.db import models


class News(models.Model):
    """Модель новости"""

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст новости")
    date_created = models.DateTimeField(
        verbose_name="Дата создания", editable=False, auto_now_add=True
    )

    def __str__(self):
        return f"{self.title}"

    def get_last_picture_url(self):
        """Возвращает url последнего изображения новости"""
        return self.pictures.last().picture.url

    def get_formatted_date_created(self):
        """Возвращает отформатированную дату создания новости"""
        return self.date_created.strftime("%d.%m.%Y")

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ["-id"]


class NewsPicture(models.Model):
    """Модель изображения новости"""

    picture = models.FileField(verbose_name="Изображение")
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name="pictures")

    def __str__(self):
        return "Изображение новости"

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class NewsComment(models.Model):
    """Модель комментария пользователя к новости"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="news_comments",
        verbose_name="Пользователь",
    )
    news = models.ForeignKey(
        "news.News",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Новость",
    )
    reply_to = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        verbose_name="Ответ к",
    )
    text = models.TextField(verbose_name="Текст")

    date_created = models.DateTimeField(verbose_name="Дата отправки", auto_now_add=True)

    def get_formatted_date_created(self):
        return self.date_created.strftime("%d.%m.%Y")

    def __str__(self):
        return f"Комментарий {self.text}"

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ["-id"]
