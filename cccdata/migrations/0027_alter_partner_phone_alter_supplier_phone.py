# Generated by Django 4.0.5 on 2022-06-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0026_rename_expense_expenses_alter_employee_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='phone',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
    ]