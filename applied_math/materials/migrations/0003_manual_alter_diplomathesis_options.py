# Generated by Django 5.0.4 on 2024-05-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_diplomathesis_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема')),
                ('file', models.FileField(upload_to='theses', verbose_name='Файл')),
                ('author_surname', models.CharField(max_length=255, verbose_name='Фамилия автора')),
                ('author_name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('author_patronymic', models.CharField(max_length=255, verbose_name='Отчество автора')),
                ('date_upload', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
            options={
                'verbose_name': 'дипломная работа',
                'verbose_name_plural': 'дипломные работы',
            },
        ),
        migrations.AlterModelOptions(
            name='diplomathesis',
            options={'verbose_name': 'дипломная работа', 'verbose_name_plural': 'дипломные работы'},
        ),
    ]
