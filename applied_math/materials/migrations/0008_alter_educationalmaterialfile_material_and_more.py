# Generated by Django 5.0.4 on 2024-06-09 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0007_remove_educationalmaterial_file_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationalmaterialfile",
            name="material",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="files",
                to="materials.educationalmaterial",
            ),
        ),
        migrations.AlterField(
            model_name="educationalmateriallink",
            name="material",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links",
                to="materials.educationalmaterial",
            ),
        ),
    ]
