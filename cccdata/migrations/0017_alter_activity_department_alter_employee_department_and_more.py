# Generated by Django 4.0.5 on 2022-06-26 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0016_alter_expenses_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('FD', 'Food/Kitchen'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('FD', 'Food/Kitchen'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('FD', 'Food/Kitchen'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='peformance',
            name='department',
            field=models.CharField(choices=[('Mn', 'Management'), ('FD', 'Food/Kitchen'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True),
        ),
    ]