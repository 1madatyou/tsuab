from django.db import models


class SupportTicket(models.Model):
    """Модель обращения в службу поддержки"""
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"