# Generated by Django 5.0.4 on 2024-05-20 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.CreateModel(
            name='EmployeeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тип')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='contacts.employee', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
