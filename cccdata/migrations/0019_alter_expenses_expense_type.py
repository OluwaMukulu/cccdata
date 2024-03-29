# Generated by Django 4.0.5 on 2022-06-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0018_remove_expenses_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expense_type',
            field=models.CharField(choices=[('EO', 'Extra Over'), ('AC', 'Accomodation'), ('CA', 'Communication/Airtime'), ('KT', 'Kitchen'), ('BD', 'Budget'), ('ME', 'Materials and Equipment'), ('FI', 'Food Items'), ('DM', 'Damages'), ('VM', 'Vehicle repair and Maintenance'), ('GS', 'Gas'), ('LB', 'Labor'), ('TX', 'Tax'), ('UN', 'Uniform')], max_length=2),
        ),
    ]
