# Generated by Django 5.0.4 on 2024-06-10 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0009_remove_educationalmaterial_date_upload_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="educationalmaterial",
            name="title_en",
        ),
        migrations.RemoveField(
            model_name="educationalmaterial",
            name="title_ru",
        ),
    ]
