# Generated by Django 4.0.5 on 2022-06-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0014_alter_expenses_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
