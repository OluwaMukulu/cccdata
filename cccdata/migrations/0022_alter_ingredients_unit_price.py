# Generated by Django 4.0.5 on 2022-06-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0021_alter_ingredients_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
