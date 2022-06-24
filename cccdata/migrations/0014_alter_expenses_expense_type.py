# Generated by Django 4.0.5 on 2022-06-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0013_alter_activity_description_alter_activity_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expense_type',
            field=models.CharField(choices=[('EO', 'Extra Over'), ('AC', 'Accomodation'), ('CA', 'Communication/Airtime'), ('KT', 'Kitchen'), ('ME', 'Materials and Equipment'), ('FI', 'Food Items'), ('DM', 'Damages'), ('VM', 'Vehicle repair and Maintenance'), ('GS', 'Gas'), ('LB', 'Labor'), ('UN', 'Uniform')], max_length=2),
        ),
    ]
