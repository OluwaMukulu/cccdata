# Generated by Django 4.0.5 on 2022-06-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0009_alter_peformance_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='menu',
        ),
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('HN', 'Has not started'), ('ST', 'Started'), ('TF', '25%'), ('FT', '50%'), ('SF', '75%'), ('CP', 'Completed')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='peformance',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
    ]