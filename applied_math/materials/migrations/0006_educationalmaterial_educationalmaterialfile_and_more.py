# Generated by Django 5.0.4 on 2024-06-07 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_diplomathesis_title_en_diplomathesis_title_ru_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EducationalMaterial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Тема")),
                (
                    "title_ru",
                    models.CharField(max_length=255, null=True, verbose_name="Тема"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=255, null=True, verbose_name="Тема"),
                ),
                ("file", models.FileField(upload_to="theses", verbose_name="Файл")),
                (
                    "date_upload",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата загрузки"
                    ),
                ),
            ],
            options={
                "verbose_name": "материал для обучения",
                "verbose_name_plural": "обучающие материалы",
            },
        ),
        migrations.CreateModel(
            name="EducationalMaterialFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "title_ru",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "title_en",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Название"
                    ),
                ),
                ("file", models.FileField(upload_to="educational_materials")),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.educationalmaterial",
                    ),
                ),
            ],
            options={
                "verbose_name": "файл",
                "verbose_name_plural": "файлы",
            },
        ),
        migrations.CreateModel(
            name="EducationalMaterialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "title_ru",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "title_en",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Название"
                    ),
                ),
                ("href", models.URLField()),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.educationalmaterial",
                    ),
                ),
            ],
            options={
                "verbose_name": "ссылка",
                "verbose_name_plural": "ссылки",
            },
        ),
    ]
