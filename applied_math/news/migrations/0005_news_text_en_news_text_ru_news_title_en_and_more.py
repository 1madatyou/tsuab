# Generated by Django 5.0.4 on 2024-05-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_options_alter_newspicture_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
