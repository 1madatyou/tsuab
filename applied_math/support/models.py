from django.db import models


class SupportTicket(models.Model):
    """Модель обращения в службу поддержки"""
    user_name = models.CharField(verbose_name='Имя пользователя', max_length=255)
    user_email = models.EmailField()
    subject = models.CharField(verbose_name="Тема", max_length=255)
    text = models.TextField(verbose_name="Текст")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения" 