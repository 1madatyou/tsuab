# Generated by Django 5.0.4 on 2024-05-05 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="diplomathesis",
            options={
                "verbose_name": "Дипломная работа",
                "verbose_name_plural": "Дипломные работы",
            },
        ),
    ]
