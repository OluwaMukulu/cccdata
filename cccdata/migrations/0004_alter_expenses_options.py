# Generated by Django 4.0.5 on 2022-06-22 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0003_alter_employee_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['name', 'description', 'supplier', 'department', 'event', 'activity', 'date', 'expense_type', 'unit_price', 'quantity', 'order_status', 'payment_method'], 'verbose_name_plural': 'Expenses'},
        ),
    ]
