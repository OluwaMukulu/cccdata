# Generated by Django 4.0.5 on 2022-06-22 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0004_alter_expenses_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'verbose_name_plural': 'Expenses'},
        ),
    ]
