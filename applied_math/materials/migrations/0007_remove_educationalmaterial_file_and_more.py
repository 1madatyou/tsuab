# Generated by Django 5.0.4 on 2024-06-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_educationalmaterial_educationalmaterialfile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalmaterial',
            name='file',
        ),
        migrations.AlterField(
            model_name='educationalmaterialfile',
            name='file',
            field=models.FileField(upload_to='educational_materials', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='educationalmateriallink',
            name='href',
            field=models.URLField(verbose_name='Ссылка'),
        ),
    ]
