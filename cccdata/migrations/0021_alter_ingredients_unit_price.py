# Generated by Django 4.0.5 on 2022-06-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0020_expense_alter_employee_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]
