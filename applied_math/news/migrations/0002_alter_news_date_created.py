# Generated by Django 5.0.4 on 2024-04-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
    ]
