# Generated by Django 5.0.4 on 2024-05-21 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_manual_alter_diplomathesis_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="manual",
            options={
                "verbose_name": "методическое указание",
                "verbose_name_plural": "методические указания",
            },
        ),
    ]
