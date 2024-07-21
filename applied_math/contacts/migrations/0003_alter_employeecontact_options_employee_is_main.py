# Generated by Django 5.0.4 on 2024-05-20 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_alter_employee_options_employeecontact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="employeecontact",
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты сотрудника",
            },
        ),
        migrations.AddField(
            model_name="employee",
            name="is_main",
            field=models.BooleanField(default=0),
        ),
    ]
